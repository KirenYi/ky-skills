# 数据源说明

## 当前默认：`nitter_rss`

- 请求：`{instance}/{handle}/rss`
- 默认实例：`https://nitter.net`（可在 config 里配置列表，失败自动换下一个）
- **优点**：无需 X API Key、实现简单  
- **缺点**：实例会挂、可能验证码、通常只有最近约 20 条、字段不完整

### 配置多个镜像

```json
"nitter_instances": [
  "https://nitter.net"
]
```

按顺序尝试；成功的实例会优先用于下一次。

## 计划中：`x_api`

官方 [X API pay-per-use](https://docs.x.com/x-api/getting-started/pricing)：

- 读帖约按资源计费（文档中 Posts: Read 量级约 $0.005/条，以控制台为准）
- 适合：稳定生产、历史回填、多博主长期跑

接入后 `config.source` 设为 `x_api`，并提供 token（环境变量，勿写入 git）。

## 可选：开源语料导入

部分博主会自己开源结构化摘录（例如知识原子 JSONL）。  
那是**另一条回填路径**，不是默认 sync 流程；适合一次性补历史观点，不适合替代增量监控。

## 合规

- 只处理**公开**帖子  
- 默认个人学习归档  
- 不要把本工具包装成绕过平台限制的爬虫服务  
