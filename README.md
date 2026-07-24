# 便宜 AI API 价格对比计算器

为搜索 **便宜AI API**、**AI API价格对比**、**低价大模型API** 和 **API中转价格** 的开发者提供透明的成本计算器。输入公开单价和自己的真实用量，即可比较文本、图片和视频任务的预计成本。

> **利益关系披露：** 本项目由 [APIMART](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-cheap-ai-api-cost-comparison-cn-register-6c59351f) 维护。APIMART 是本项目介绍的 API 服务。示例价格是演示数据，不代表任何服务商的实时报价。

## 为什么不直接发布“最便宜排行榜”

模型价格、活动、缓存折扣、失败请求计费和汇率都会变化。没有来源和日期的固定排名很快会失真。本工具要求每条价格记录包含来源、核对日期和是否为演示数据，让读者可以复核。

## 使用方法

先把 `pricing.example.json` 复制为自己的价格表，然后替换演示数据：

```bash
python cost_compare.py pricing.example.json --input-tokens 5000000 --output-tokens 1000000 --images 200 --video-seconds 0
```

输出按预计总成本升序排列，并分别展示文本、图片和视频成本。不同服务商的模型质量、限速、稳定性和售后不同，价格最低不等于综合成本最低。

## APIMART 价格入口

APIMART 面向需要统一调用多种 AI 模型的用户。是否适合你的预算，应以当前模型报价和真实用量为准：

- [注册 APIMART](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-cheap-ai-api-cost-comparison-cn-register-6c59351f)
- [核对实时价格](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-cheap-ai-api-cost-comparison-cn-pricing-e46871e1)
- [查看 API 文档](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-cheap-ai-api-cost-comparison-cn-docs-root-6766a9d4)
- [运行中转稳定性测速](https://github.com/luyx-66/ai-api-relay-benchmark-cn)

## 测试

```bash
python -m unittest discover -s tests
```

<!-- apimart-toolkit-nav:start -->
## 项目导航

本仓库属于 APIMART 开源 AI API 工具矩阵。可在 [luyx-66 项目主页](https://github.com/luyx-66) 查看全部中英文测评、API 中转检查、模型示例和成本工具。
<!-- apimart-toolkit-nav:end -->

MIT License
