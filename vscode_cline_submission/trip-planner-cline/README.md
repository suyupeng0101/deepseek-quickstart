
# Trip Planner (CLINE + VS Code 示例项目)

## 项目说明
该项目演示如何在 VS Code + CLINE 环境下集成 12306 MCP Server 与 中国天气 MCP Server，构建简单的行程规划助手。

包含：
- app.py: Flask 后端提供 POST /plan 接口，调用 12306 MCP 和 中国天气 MCP，返回合并的行程与天气数据。
- mock_12306_mcp.py: 本地 mock 12306 MCP HTTP 服务（便于开发）
- mock_cn_weather.py: 本地 mock 中国天气 MCP HTTP 服务（便于开发）
- config.example.json: 配置示例

## 快速启动（开发）
1. 安装依赖：
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\\Scripts\\activate  # Windows
   pip install -r requirements.txt
   ```
2. 启动 mock servers（各开一个终端）：
   ```bash
   python mock_12306_mcp.py
   python mock_cn_weather.py
   ```
3. 运行后端：
   ```bash
   python app.py
   ```
4. 测试示例：
   ```bash
   curl -X POST http://localhost:5002/plan -H "Content-Type: application/json" -d '{"origin":"Beijing","destination":"Shanghai","date":"2025-09-10","preferences":"最快"}'
   ```

## 在 VS Code + CLINE 中开发（建议）
1. 打开本项目文件夹。
2. 使用课程提供的 CLINE 插件/CLI 注册上面启动的 mock MCP 服务，或直接在 CLINE 中配置 HTTP 类型的 MCP Server（地址指向 mock 服务）。
3. 在 VS Code 中调试 app.py，或使用 CLINE 在终端中直接调用 MCP Tools 并验证与 Flask 后端的集成。

## 提交
将该项目上传到 GitHub/Gitee 并将仓库链接粘贴到作业提交框。
