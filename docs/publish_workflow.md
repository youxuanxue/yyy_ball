# 自动发布脚本执行流程

## 整体流程概览

自动发布脚本分为两个主要部分：
1. **`publish_lesson.py`** - 主入口脚本，负责准备数据和初始化
2. **`wx_channel.py`** - 发布器类，负责浏览器自动化操作

---

## 详细执行顺序

### 阶段一：数据准备 (`publish_lesson.py`)

#### 1. 参数解析
- 解析命令行参数：`lesson_path` 和 `--debug`
- 示例：`sunzi/lesson08` → 解析为 `series_name="sunzi"`, `lesson_dir_name="lesson08"`

#### 2. 路径验证
- 验证课程目录是否存在：`series/{series_name}/{lesson_dir_name}`
- 验证媒体目录是否存在：`series/{series_name}/{lesson_dir_name}/media`

#### 3. 查找视频文件
- 查找路径：`lesson/media/videos/animate/1920p60/`
- 优先查找：`*Vertical.mp4`
- 备选：`*.mp4`
- 如果找不到，脚本终止

#### 4. 读取元数据 (`script.json`)
- 读取 `script.json` 文件
- 提取 `wechat` 字段：
  - `title` - 视频标题（限制16字符，超长自动截断）
  - `description` - 视频描述
  - `hashtags` - 话题标签（自动追加到描述末尾）
- 如果缺少必要字段，脚本终止

#### 5. 初始化发布器
- 创建 `WeChatChannelPublisher` 实例
- 设置 `headless=False`（显示浏览器）
- 设置 `auth_path` 为项目根目录（使用 `config/auth_wx.json`）
- 如果启用 `--debug`，会生成调试截图和HTML文件

---

### 阶段二：浏览器初始化 (`wx_channel.py` - `start()`)

#### 6. 启动 Playwright
- 启动 Playwright 引擎
- 启动 Chromium 浏览器（最大化窗口）

#### 7. 加载认证状态
- 检查 `config/auth_wx.json` 是否存在
- 如果存在：加载已保存的认证状态（避免重复登录）
- 如果不存在：创建新的浏览器上下文

#### 8. 创建页面
- 创建新的浏览器标签页

---

### 阶段三：登录验证 (`wx_channel.py` - `login()`)

#### 9. 导航到微信视频号
- 访问：`https://channels.weixin.qq.com`
- 等待页面加载完成

#### 10. 检查登录状态
- 检查 URL 是否包含 `login`
- **如果未登录**：
  - 显示二维码
  - 等待用户扫码（最多60秒）
  - 检测到登录后保存认证状态
- **如果已登录**：
  - 直接继续

---

### 阶段四：发布操作 (`wx_channel.py` - `publish()`)

#### 11. 任务验证
- 验证视频文件是否存在
- 验证封面文件（如果提供）是否存在

#### 12. 导航到创建页面
- 访问：`https://channels.weixin.qq.com/platform/post/create`
- 等待页面加载完成
- 检查是否被重定向到登录页（会话过期）

#### 13. 上传视频
- 查找文件输入框：`input[type="file"]`
- 设置视频文件路径
- 开始上传视频
- 等待上传开始（生成调试截图）

#### 14. 等待上传完成
- 硬等待 10 秒（让上传开始并稳定）
- 等待描述编辑器出现（最多等待 300 秒）

#### 15. 填写视频描述
- 查找描述编辑器：`div.input-editor` 或 `div[data-placeholder="添加描述"]`
- 点击编辑器
- 输入描述内容（包含话题标签）

#### 16. 填写视频标题
- 查找标题输入框：`input.weui-desktop-form__input[placeholder*="概括视频主要内容"]`
- 如果输入框可见，填写标题
- 如果不可见，跳过（记录警告）

#### 17. 选择合集《我是小小谋略家》
- 尝试多种选择器查找合集选择器：
  - `text=选择合集`
  - `text=合集`
  - `button:has-text("合集")`
  - `.collection-selector`
  - `[placeholder*="合集"]`
- 点击合集选择器
- 等待下拉菜单/弹窗出现（1秒）
- **策略A**：直接在列表中查找"我是小小谋略家"并点击
- **策略B**：如果找不到，使用搜索框搜索"我是小小谋略家"，然后点击
- 如果找不到，记录警告（不中断流程）

#### 18. 搜索并参加活动
- 尝试多种选择器查找活动按钮：
  - `text=参加活动`
  - `text=活动`
  - `button:has-text("活动")`
  - `.activity-selector`
  - `[placeholder*="活动"]`
- 点击活动按钮
- 等待活动弹窗出现（1秒）
- **搜索策略**：使用关键词搜索活动：
  - 全网征集小小谋略家
- 搜索过程：
  - 查找搜索输入框
  - 输入关键词
  - 等待搜索结果（2秒）
  - 尝试点击第一个活动结果
  - 如果成功，停止搜索
- **备选策略**：如果找不到搜索框，直接点击第一个可用活动
- 如果找不到或参加失败，记录警告（不中断流程）

#### 19. 勾选原创（放在最后避免弹窗干扰）
- 尝试多种选择器查找"原创"复选框：
  - `input[type="checkbox"]:near(text="原创")`
  - `label:has-text("原创") input[type="checkbox"]`
  - `input[type="checkbox"]`
  - `.weui-desktop-checkbox:has-text("原创")`
  - `text=原创`
- 如果找到且未勾选，则勾选
- 如果已勾选，跳过
- 如果找不到，记录警告（不中断流程）
- **注意**：此步骤放在选择合集和参加活动之后，避免弹窗遮挡复选框

#### 20. 完成准备（不实际发布）
- 记录日志："DRY RUN: Ready to publish. Skipping actual click on 'Publish' button."
- 等待 5 秒（让用户观察结果）
- **注意**：脚本不会自动点击"发表"按钮，需要用户手动确认

---

### 阶段五：用户确认 (`publish_lesson.py`)

#### 21. 等待用户确认
- 显示提示："脚本执行完毕，请检查浏览器窗口。"
- 显示提示："请在浏览器中确认发布信息。完成后按回车键关闭浏览器..."
- **交互式环境**：等待用户按回车键
- **非交互式环境**：等待 5 分钟后自动关闭

#### 22. 保存认证状态并关闭
- 保存浏览器认证状态到 `config/auth_wx.json`
- 关闭浏览器
- 关闭 Playwright

---

## 关键时间点

| 步骤 | 等待时间 | 说明 |
|------|---------|------|
| 上传视频后 | 10秒 | 硬等待，让上传开始 |
| 描述编辑器 | 最多300秒 | 等待编辑器出现 |
| 合集选择 | 1秒 | 等待下拉菜单出现 |
| 活动搜索 | 2秒 | 等待搜索结果 |
| 完成准备 | 5秒 | 让用户观察结果 |
| 用户确认 | 用户控制 | 等待用户按回车 |

---

## 错误处理策略

### 阻塞性错误（会终止脚本）
- 视频文件不存在
- `script.json` 不存在或格式错误
- 缺少必要的元数据字段
- 浏览器启动失败
- 登录失败或超时
- 上传视频失败
- 填写描述失败

### 非阻塞性错误（记录警告，继续执行）
- 勾选原创失败
- 选择合集失败
- 参加活动失败

这些非阻塞性错误不会中断发布流程，但会在日志中记录警告，用户可以手动完成这些步骤。

---

## 调试模式 (`--debug`)

启用 `--debug` 参数后，会在以下位置生成调试文件：

1. `create_page_loaded.png` - 创建页面加载后的截图
2. `create_page_debug.html` - 创建页面的HTML源码
3. `upload_start_debug.png` - 上传开始时的截图
4. `publish_error.png` - 发布错误时的截图
5. `login_error.png` - 登录错误时的截图
6. `session_expired.png` - 会话过期时的截图

---

## 使用示例

```bash
# 基本使用
uv run src/publish/publish_lesson.py sunzi/lesson08

# 启用调试模式
uv run src/publish/publish_lesson.py sunzi/lesson08 --debug
```

