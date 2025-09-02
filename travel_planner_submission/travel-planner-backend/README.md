
# Travel Planner Assistant (基于 DeepSeek-V3 + 12306 MCP 示例)

此项目是作业交付范例 —— 一个最小可运行的旅行规划助手后端示例。
它展示如何把 12306 MCP 服务与 DeepSeek（通过 Ollama 的本地 REST API）结合，生成结构化旅行建议。

## 文件说明
- app.py - Flask 后端示例，提供 /plan 接口
- config.example.json - 示例配置（填写 Ollama 与 12306 MCP 的地址后复制为 config.json）
- requirements.txt - Python 依赖

## 快速运行（开发环境）
1. 在本机安装 Python3.10+，创建虚拟环境并激活：
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows (PowerShell)
   pip install -r requirements.txt
   ```
2. 将 `config.example.json` 复制为 `config.json`，并根据你的环境修改：
   - OLLAMA_API: Ollama 的 REST 地址，通常 `http://localhost:11434`
   - OLLAMA_MODEL: 使用的模型名，例如 `deepseek-v3`
   - MCP_12306_URL: 12306 MCP Server 的 HTTP 地址，例如 `http://localhost:8080`
3. 启动后端：
   ```bash
   python app.py
   ```
4. 测试（示例）：
   ```bash
   curl -X POST http://localhost:5000/plan -H "Content-Type: application/json" -d '{"origin":"Beijing","destination":"Shanghai","date":"2025-09-10","preferences":"最快"}'
   ```

## 关于环境准备（关键步骤要点）
1. 安装 Cherry Studio（桌面客户端）并在设置中添加 MCP Servers/Clients（参考 Cherry Studio GitHub releases）。
2. 安装并运行 12306 MCP Server（仓库示例可用 npx 启动或用 Docker 运行，参见 12306-mcp 项目文档）。
3. 安装 Ollama 并拉取 DeepSeek-V3（或可用的 DeepSeek 模型），并确保 Ollama 的 REST 服务可访问（默认 11434 端口）。
4. 在 Cherry Studio 中注册 MCP Server（把 12306 MCP Server 的启动命令或 HTTP 地址加入 MCP 配置），并允许联网模式（如果需要让模型调用外部 HTTP 接口）。

## 注意事项
- Ollama 与 DeepSeek 模型可能需要额外的硬件与磁盘空间，请查阅 DeepSeek 与 Ollama 的安装说明。
- 12306 MCP 项目展示了如何把中国铁路数据包装为 MCP 工具，具体接口名称请以你使用的 MCP Server 仓库为准。

## 将代码上传至 GitHub/Gitee
1. 在 GitHub/Gitee 新建仓库（例如 travel-planner），然后按常规 git 流程推送。示例命令：
   ```bash
   git init
   git add .
   git commit -m "feat: add travel-planner example (DeepSeek + 12306 MCP)"
   git remote add origin git@github.com:你的用户名/travel-planner.git
   git branch -M main
   git push -u origin main
   ```

## 作业提交说明（复制到你的在线文档底部）
- 本仓库（示例）地址（请替换为你的实际仓库地址）：
  - https://github.com/你的用户名/travel-planner

- 在线文档（请把本 README 的关键步骤整理并粘贴到 Word / Notion，并将文档设置为公开阅读）
