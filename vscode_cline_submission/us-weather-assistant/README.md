
# US Weather Assistant (基于 CLINE + VS Code 开发环境示例)

## 项目说明
这是一个最小示例项目，展示如何在 VS Code + CLINE 开发环境下实现一个“美国天气助手”。
- /weather : Flask GET endpoint，查询配置的 US_WEATHER_MCP_URL 并返回结果
- mock_us_mcp.py : 用于本地测试的模拟 MCP Server

## 快速启动（本地开发）
1. 创建虚拟环境并安装依赖：
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\\Scripts\\activate  # Windows PowerShell
   pip install -r requirements.txt
   ```
2. 启动 mock MCP（可选，用于开发）：
   ```bash
   python mock_us_mcp.py
   ```
3. 运行应用：
   ```bash
   python weather.py
   ```
4. 测试（另开终端）
   ```bash
   curl 'http://localhost:5001/weather?city=San Francisco'
   ```

## 在 VS Code 中使用 CLINE 开发（说明）
1. 在 VS Code 中打开本项目文件夹。
2. 安装并配置 CLINE 插件/CLI（课程提供的说明）。
3. 使用 CLINE 在 VS Code 终端中注册/调用 MCP（例如本地 mock MCP）。
4. 在 .vscode/launch.json 中配置调试任务（本项目已提供一个示例）。

## 提交
请把该项目上传至 GitHub/Gitee，仓库 README 保留本说明。
