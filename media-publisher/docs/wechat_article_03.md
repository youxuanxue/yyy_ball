# YouTube发布失败？一个土木狗和「网络问题」死磕的一天

---

## 开头先吐槽一句

我真的服了。

一个「发布到YouTube」的功能，愣是让我折腾了一整个下午。

代码没问题、网络没问题、代理也开着——就是死活连不上YouTube的服务器。

最后怎么解决的？往下看，我把踩过的每一个坑都记下来了，省得你再踩一遍。

---

## 回顾一下

上篇文章说到，我的「火箭发射」工具升级到了2.0版本，支持同时发布到微信视频号和YouTube。

当时写那篇文章的时候，YouTube功能其实还没真正测过。

毕竟代码是AI帮我写的，我只是看了看界面，觉得「应该没问题吧」。

结果...

---

## 翻车现场

那天下午，我信心满满地准备测试YouTube发布功能。

视频文件：准备好了。
配置文件：写好了。
标题描述：填好了。

点击「发布」——

然后就开始转圈圈。

转啊转，转啊转...

**「[ERROR] 网络错误: [Errno 60] Operation timed out」**

啥？超时？

我看了眼WiFi图标，满格啊。打开B站，刷刷的。

再点发布，还是超时。

我当时第一反应是：完了，代码有bug。

---

## 开始排查

我把错误信息复制给AI，问它怎么回事。

AI说：「这个错误说明无法连接到YouTube的服务器。你在中国大陆吗？可能需要代理。」

哦对，YouTube在国内是访问不了的，这我知道。

但我电脑上明明开着代理软件啊？平时看YouTube视频都没问题。

AI又说：「程序可能没有走代理。试试设置环境变量HTTP_PROXY。」

好，我按它说的，在终端里敲了一堆命令：

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

再运行，还是超时。

我心态开始有点崩了。

---

## 转折点：curl能通，Python不行？

AI让我测试一下代理是不是真的能用：

```bash
curl -x http://127.0.0.1:7890 -I https://www.googleapis.com/youtube/v3/
```

结果返回了：

```
HTTP/1.1 200 Connection established
HTTP/2 404
```

能连上！说明代理本身没问题。

那为什么Python程序跑不通？

我又用Python测试：

```python
import urllib.request
import os
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
urllib.request.urlopen('https://www.googleapis.com/youtube/v3/')
```

也返回了404（404是正常的，说明连上了）。

**所以Python本身是能走代理的，问题出在Google的API库上。**

这下我DNA动了——同一台电脑、同一个代理、同一个地址，curl能通、Python能通，偏偏那个库不行？

---

## 深挖：httplib2这个坑

经过AI一顿分析，终于找到了原因：

Google的API库（google-api-python-client）底层用的是一个叫`httplib2`的HTTP库。

这个库有个特点——**它不读环境变量里的代理设置**！

是的，你没看错。你设置了`HTTP_PROXY`、`HTTPS_PROXY`、大写小写都设了，它完全不理你。

我当时的表情：🙃

AI说可以通过代码强制让它走代理，于是开始了漫长的尝试：

- 尝试1：用`httplib2.ProxyInfo`设置代理 → 不行
- 尝试2：Monkey-patch `httplib2.Http` → 还是不行  
- 尝试3：用`proxy_info_from_url` → 依然不行

每次都是「应该可以了吧」，然后「Operation timed out」。

从下午3点搞到6点，人都麻了。

---

## 最终方案

最后，AI提出了一个「曲线救国」的方案：

**不用httplib2，换成requests库。**

requests库会乖乖读取环境变量里的代理设置。

具体做法是写一个适配器，让它「假装」自己是httplib2，但实际上用requests发请求：

```python
class RequestsHttpAdapter:
    """用requests库替代httplib2，正确支持代理"""
    
    def __init__(self, credentials=None, timeout=1800):
        self.session = requests.Session()
        # requests会自动读取HTTPS_PROXY环境变量
        proxy_url = os.environ.get('HTTPS_PROXY', '')
        if proxy_url:
            self.session.proxies = {
                'http': proxy_url,
                'https': proxy_url
            }
```

换上这个适配器之后——

**「[INFO] 📊 上传进度: 94%」**
**「[INFO] ✅ 视频上传成功！」**

那一刻，我差点哭出来。

---

## 说说代理这件事

折腾了一下午，我对「代理」这个东西有了更深的理解。

### 为什么需要代理？

简单说，有些网站在国内是打不开的（你懂的）。

如果你想做YouTube、用Google服务、访问海外工具，代理是绑定需求。

### 代理的几种姿势

1. **VPN软件**：一键开启，全局走代理（最简单）
2. **设置环境变量**：让终端里的程序走代理
3. **代码里强制设置**：针对某些「不听话」的库

### 我踩的坑

我的VPN软件开着，浏览器能正常访问YouTube。

但问题是，VPN默认只代理浏览器流量，终端里的程序不走代理。

需要额外设置「系统代理」或者「TUN模式」，或者手动设环境变量。

而就算设了环境变量，还得看程序愿不愿意读取...（说的就是你，httplib2）

### 我用的代理服务

既然聊到这儿，分享一下我自己用的代理。

作为「1人公司」，我对工具的要求就俩字：**稳定**。

折腾了半天连不上，时间成本太高了。

我目前用的是 [Shadowsocks](https://secure.shadowsocks.au/aff.php?aff=83130)，用了一年多，体验还行：

- 连接稳定，基本没断过
- 速度够用，YouTube 1080p无压力
- 多设备支持，电脑手机都能用

如果你也有出海需求（做YouTube、用ChatGPT、访问Google服务等），可以考虑。

当然，市面上选择很多，找一个稳定的就行。**别为了省几十块钱，结果折腾一下午**，得不偿失。

---

## 给大家的实操指南

如果你也要做YouTube发布，这里是我总结的checklist：

### 1. 测试代理是否能用

```bash
# 把7890换成你的代理端口
curl -x http://127.0.0.1:7890 -I https://www.googleapis.com/youtube/v3/
```

看到 `200 Connection established` 就说明代理通了。

### 2. 设置环境变量

```bash
# 在 ~/.zshrc 或 ~/.bashrc 里加上：
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```

大写小写都设上，因为不同程序读的不一样。

### 3. 常见报错

| 报错 | 原因 | 解决 |
|------|------|------|
| Operation timed out | 代理没生效 | 检查代理是否开启、环境变量是否设置 |
| Connection refused | 代理端口错误 | 确认代理软件的端口号 |
| 407 Proxy Authentication | 代理需要密码 | 用带密码格式：`http://user:pass@host:port` |

---

## 写在最后

4个小时，就为了让一个程序能「翻出去」。

值吗？

说实话，当时挺上头的，就想搞明白到底哪儿出了问题。

现在回头看，还真学到不少东西——环境变量怎么回事、代理怎么工作的、为什么有的库这么「轴」不读配置...

搞技术这事儿吧，和我以前在工地干活差不多：

**坑，你不踩一遍，永远不知道有多深。**

**踩完了，下次就知道绕着走了。**

我把坑都记下来了，你就别再踩了，直接绕。

---

**🔥 关注「懿起成长」**，持续分享：
- AI 搞钱实战
- 技术踩坑记录
- 1 人公司效率心得

**💬 加入「1 人公司互助群」**：

> 🌟 本群宗旨：**资源互换、共同搞钱，告别单打独斗。**
> 
> 🤝 只要大家聚在一起，就没有解决不了的难题，也没有搞不到的钱！

- 后台回复「**火箭**」，获取工具
- 后台回复「**搞钱**」，加入互助群

---

**你有遇到过什么「网络问题」的坑吗？**

评论区聊聊，说不定我踩过同款！

**和气生财，互帮互助，祝大家出海顺利，搞钱无阻！🚀🚀🚀**

---

*一个正在用 AI 搞钱的土木工程师*  
*「懿起成长」主理人*  
*日日生金日日福*

---

## 📦 本文提到的工具

| 工具 | 用途 | 链接 |
|------|------|------|
| 火箭发射 | 视频多平台发布 | 后台回复「火箭」获取 |
| Shadowsocks | 稳定的代理服务 | [点击查看](https://secure.shadowsocks.au/aff.php?aff=83130) |
| Cursor | AI编程助手 | 搜索即可下载 |
