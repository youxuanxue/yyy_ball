# creator 工作台

`creator` 是迁移到 `yyy_ball` 的内容策划工作台，负责三段式流程：

1. 抓取公众号文章数据。
2. 分析目标账号与参考账号内容特征。
3. 生成可审阅、可继续改写成视频脚本的内容规划。

## 为什么不直接原样合并上游 `creator/`

上游实现是一个独立 `uv` 子项目，适合单独跑公众号规划，但直接并入当前仓库会带来三个问题：

- 会引入第二个 `pyproject.toml`，和当前根项目环境重复。
- 路径与认证状态默认指向上游目录约定，不符合 `yyy_ball` 的工作区结构。
- 分析器和规划器写死了育儿账号设定，不适合当前仓库的兵法/财商内容方向。

当前迁移后的版本做了三类修正：

- 代码落在 `src/creator/`，继续复用根项目依赖，不新增子项目。
- 配置与输出落在顶层 `creator/`，与 `series/` 内容产物解耦。
- 分析器、规划器改为配置驱动，并支持离线 mock 响应测试。

## 快速使用

先修改 `creator/config/target.json`，再执行：

```bash
uv run python -m src.creator analyze
uv run python -m src.creator plan -y --mock-response-file /path/to/mock_response.txt
```

如需真实抓取公众号：

```bash
uv run python -m src.creator scrape
```

首次运行会打开 `mp.weixin.qq.com` 并等待扫码登录，认证状态会保存到 `~/.yyy_ball/creator/gzh_auth.json`。

## 目录

```text
creator/
├── README.md
├── ARCHITECTURE_REVIEW.md
├── config/
│   └── target.json
└── output/
```
