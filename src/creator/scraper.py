"""WeChat Official Account article scraper for creator workflows."""

from __future__ import annotations

import json
import logging
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Callable
from typing import Optional
from urllib.parse import urlencode

from playwright.sync_api import BrowserContext
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)

AUTH_DIR = Path.home() / ".yyy_ball" / "creator"
AUTH_FILE = AUTH_DIR / "gzh_auth.json"


def _ts_to_date(ts: int) -> str:
    if not ts:
        return ""
    try:
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except Exception:
        return ""


class GzhScraper:
    """Scrape article metadata and article detail pages from mp.weixin.qq.com."""

    BASE_URL = "https://mp.weixin.qq.com"

    def __init__(
        self,
        headless: bool = False,
        log_fn: Optional[Callable[[str], None]] = None,
    ):
        self.headless = headless
        self._log_fn = log_fn or (lambda message: logger.info(message))
        self._playwright = None
        self._browser = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None
        self._token: Optional[str] = None

    def _log(self, message: str) -> None:
        self._log_fn(message)

    def start(self) -> None:
        self._log("正在启动浏览器...")
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(
            headless=self.headless, args=["--start-maximized"]
        )
        AUTH_DIR.mkdir(parents=True, exist_ok=True)

        if AUTH_FILE.exists():
            self._log(f"加载登录状态: {AUTH_FILE}")
            self._context = self._browser.new_context(
                storage_state=str(AUTH_FILE), no_viewport=True
            )
        else:
            self._log("未找到登录状态，需要扫码登录")
            self._context = self._browser.new_context(no_viewport=True)

        self._page = self._context.new_page()

    def close(self) -> None:
        if self._context:
            try:
                self._context.storage_state(path=str(AUTH_FILE))
                self._log(f"登录状态已保存: {AUTH_FILE}")
            except Exception as exc:
                self._log(f"保存登录状态失败: {exc}")
            self._context.close()
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()
        self._log("浏览器已关闭")

    def __enter__(self) -> "GzhScraper":
        self.start()
        return self

    def __exit__(self, *_args) -> None:
        self.close()

    def authenticate(self, timeout: int = 120) -> None:
        if not self._page:
            raise RuntimeError("浏览器尚未启动")

        self._log("正在打开微信公众号后台...")
        self._page.goto(self.BASE_URL, timeout=60000)
        self._page.wait_for_load_state("domcontentloaded")
        logged_in_selector = ".new-creation__menu, .weui-desktop-layout__main"

        if AUTH_FILE.exists():
            try:
                if self._page.locator(logged_in_selector).first.is_visible(timeout=5000):
                    self._log("已登录")
                    self._extract_token()
                    return
            except Exception:
                pass

        self._log("请在浏览器中扫码登录微信公众号...")
        try:
            self._page.wait_for_selector(
                logged_in_selector, state="visible", timeout=timeout * 1000
            )
            self._log("登录成功")
            self._context.storage_state(path=str(AUTH_FILE))
        except Exception as exc:
            raise RuntimeError(f"等待扫码登录超时（{timeout}秒）") from exc

        self._extract_token()

    def _extract_token(self) -> None:
        if not self._page:
            raise RuntimeError("浏览器尚未启动")

        url = self._page.url
        match = re.search(r"token=(\d+)", url)
        if match:
            self._token = match.group(1)
            self._log(f"已获取 token: {self._token}")
            return

        self._page.goto(f"{self.BASE_URL}/cgi-bin/home?lang=zh_CN", timeout=30000)
        self._page.wait_for_load_state("domcontentloaded")
        time.sleep(2)
        url = self._page.url
        match = re.search(r"token=(\d+)", url)
        if match:
            self._token = match.group(1)
            self._log(f"已获取 token: {self._token}")
            return
        raise RuntimeError(f"无法从 URL 提取 token: {url}")

    def _api_get(self, path: str, params: dict) -> dict:
        if not self._token or not self._page:
            raise RuntimeError("请先完成认证")

        merged = {
            **params,
            "token": self._token,
            "lang": "zh_CN",
            "f": "json",
            "ajax": "1",
        }
        url = f"{self.BASE_URL}{path}?{urlencode(merged)}"
        return self._page.evaluate(
            """async (url) => {
                const resp = await fetch(url, { credentials: 'include' });
                return await resp.json();
            }""",
            url,
        )

    def search_account(self, name: str) -> Optional[dict]:
        self._log(f"搜索公众号: {name}")
        data = self._api_get(
            "/cgi-bin/searchbiz",
            {
                "action": "search_biz",
                "begin": "0",
                "count": "5",
                "query": name,
            },
        )
        biz_list = data.get("list", [])
        if not biz_list:
            self._log(f"未找到公众号: {name}")
            return None

        for biz in biz_list:
            if biz.get("nickname") == name:
                self._log(f"找到公众号: {biz['nickname']} (fakeid={biz['fakeid']})")
                return biz

        biz = biz_list[0]
        self._log(f"找到公众号（模糊匹配）: {biz['nickname']} (fakeid={biz['fakeid']})")
        return biz

    def get_article_list(
        self, fakeid: str, count: int = 10, max_pages: int = 50
    ) -> list[dict]:
        all_articles = []
        begin = 0
        for page_num in range(max_pages):
            self._log(f"  获取文章列表 第 {page_num + 1} 页 (begin={begin})")
            data = self._api_get(
                "/cgi-bin/appmsg",
                {
                    "action": "list_ex",
                    "begin": str(begin),
                    "count": str(count),
                    "fakeid": fakeid,
                    "type": "9",
                    "query": "",
                },
            )
            articles = data.get("app_msg_list", [])
            if not articles:
                break
            all_articles.extend(articles)
            total = data.get("app_msg_cnt", 0)
            self._log(f"  获取 {len(articles)} 篇 (累计 {len(all_articles)}/{total})")
            if len(all_articles) >= total:
                break
            begin += count
            time.sleep(1.5)
        return all_articles

    def get_article_content(self, url: str) -> dict:
        if not self._context:
            raise RuntimeError("浏览器上下文不存在")

        page = self._context.new_page()
        result = {"content": "", "read_count": 0, "like_count": 0}
        try:
            page.goto(url, timeout=30000)
            page.wait_for_load_state("domcontentloaded")
            time.sleep(2)

            result["content"] = (
                page.evaluate(
                    """() => {
                        const el = document.querySelector('#js_content');
                        return el ? el.innerText : '';
                    }"""
                )
                or ""
            ).strip()

            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)

            read_count = page.evaluate(
                """() => {
                    const el = document.querySelector('#js_read_area .read_num, .read_num_text');
                    if (!el) return 0;
                    const match = el.textContent.match(/\\d+/);
                    return match ? parseInt(match[0]) : 0;
                }"""
            )
            like_count = page.evaluate(
                """() => {
                    const selectors = [
                        '#js_like_area .like_num',
                        '.like_num_text',
                        '#js_read_like_area .like_num',
                    ];
                    for (const selector of selectors) {
                        const el = document.querySelector(selector);
                        if (!el) continue;
                        const match = el.textContent.match(/\\d+/);
                        if (match) return parseInt(match[0]);
                    }
                    return 0;
                }"""
            )
            result["read_count"] = read_count or 0
            result["like_count"] = like_count or 0
        except Exception as exc:
            self._log(f"  获取文章内容失败: {exc}")
        finally:
            page.close()
        return result

    def scrape_account_deep(
        self,
        name: str,
        output_dir: Path,
        max_pages: int = 50,
    ) -> Optional[Path]:
        account = self.search_account(name)
        if not account:
            return None

        self._log(f"\n=== 深度抓取: {name} ===")
        articles = self.get_article_list(account["fakeid"], count=10, max_pages=max_pages)
        self._log(f"共 {len(articles)} 篇文章，开始抓取正文和互动数据")
        results = []
        for index, article in enumerate(articles, start=1):
            self._log(f"  [{index}/{len(articles)}] {article.get('title', '无标题')}")
            detail = self.get_article_content(article.get("link", ""))
            results.append(
                {
                    "title": article.get("title", ""),
                    "digest": article.get("digest", ""),
                    "link": article.get("link", ""),
                    "cover": article.get("cover", ""),
                    "create_time": article.get("create_time", 0),
                    "create_date": _ts_to_date(article.get("create_time", 0)),
                    "content": detail["content"],
                    "read_count": detail["read_count"],
                    "like_count": detail["like_count"],
                }
            )
            time.sleep(2)

        output_file = output_dir / f"{name}.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        self._log(f"已保存 {len(results)} 篇文章到 {output_file}")
        return output_file

    def scrape_account_list(
        self,
        name: str,
        output_dir: Path,
        max_articles: int = 60,
        sample_detail: int = 20,
    ) -> Optional[Path]:
        account = self.search_account(name)
        if not account:
            return None

        self._log(f"\n=== 列表抓取: {name} ===")
        max_pages = max(1, (max_articles + 9) // 10)
        articles = self.get_article_list(account["fakeid"], count=10, max_pages=max_pages)
        articles = articles[:max_articles]
        results = []
        for index, article in enumerate(articles):
            entry = {
                "title": article.get("title", ""),
                "digest": article.get("digest", ""),
                "link": article.get("link", ""),
                "cover": article.get("cover", ""),
                "create_time": article.get("create_time", 0),
                "create_date": _ts_to_date(article.get("create_time", 0)),
                "read_count": 0,
                "like_count": 0,
            }
            if index < sample_detail:
                self._log(
                    f"  [{index + 1}/{min(len(articles), sample_detail)}] "
                    f"获取互动数据: {article.get('title', '无标题')[:30]}"
                )
                detail = self.get_article_content(article.get("link", ""))
                entry["read_count"] = detail["read_count"]
                entry["like_count"] = detail["like_count"]
                time.sleep(2)
            results.append(entry)

        output_file = output_dir / f"{name}.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        self._log(f"已保存 {len(results)} 篇文章到 {output_file}")
        return output_file

    def scrape_all(self, config: dict, output_dir: Path) -> None:
        articles_dir = output_dir / "articles"
        articles_dir.mkdir(parents=True, exist_ok=True)

        target = config["target"]
        self._log(f"\n{'=' * 50}")
        self._log(f"开始深度抓取目标账号: {target['name']}")
        self._log(f"{'=' * 50}")
        self.scrape_account_deep(
            target["name"],
            articles_dir,
            max_pages=target.get("max_pages", 50),
        )

        for ref in config.get("references", []):
            self._log(f"\n{'=' * 50}")
            self._log(f"开始列表抓取参考账号: {ref['name']}")
            self._log(f"{'=' * 50}")
            self.scrape_account_list(
                ref["name"],
                articles_dir,
                max_articles=ref.get("max_articles", 60),
                sample_detail=ref.get("sample_detail", 20),
            )

        self._log(f"\n全部抓取完成，数据保存在 {articles_dir}")
