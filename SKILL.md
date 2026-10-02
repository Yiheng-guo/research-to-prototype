---
name: research-to-prototype
description: 把研究证据关联到需求、用户路径、验收实验和可交互原型，保留版本与证据链。用于AI产品探索到原型验证。
license: Apache-2.0
metadata:
  compatibility: Agent Skills-compatible coding assistant; Python 3.9+. Video rendering optionally needs FFmpeg or imageio-ffmpeg.
  author: Yiheng-guo
  version: "1.0.0"
  created: "2026-10-02"
---

# 研究结果转需求与原型

输入：研究材料/访谈与证据定位、目标用户、待解决问题、平台和范围。文献/访谈是证据，不自动等同市场需求。

1. 将证据编号 E001…，标 fact/inference/unknown，记录日期、来源、方法和样本限制。拒绝“一个用户提到”跳到“所有用户需要”。
2. 建 E→R→flow→test 追溯表，每个需求写用户任务、证据、验收和最小验证方式。只有推断支持时标假设实验，先验证再扩大开发。
3. `scripts/run.py` 检查关联并生成 prototype brief 和 acceptance matrix。优先实现完整一条核心路径，包含加载/无数据/失败/纠正/完成反馈，不只做第一屏。
4. 根据实际可用工具实现 HTML/应用交互；使用真实状态更新，模拟数据和模拟提交要在界面注明。原型不得假装连接生产后端。
5. 用已发现的界面元素执行路径，检查窄屏、键盘和错误状态，保存测试证据、版本与差异。验收矩阵全部通过才称该原型功能完成；需求被证明另需用户研究。

`examples/prototype.html` 提供可离线运行的咨询澄清原型，`examples/prototype-test.js` 用实际浏览器检查核心和错误路径。脚本/原型不自动发布云端，不含 API 密钥。

## 可运行样例与来源

- 输入、实际输出、失败输入和结果见 `examples/`；使用方法和字段见 [contract.md](references/contract.md)。
- 默认中文交付；成功条件是实际任务产物和检查记录齐全，格式通过不能替代内容验证。
- 开源来源、固定 commit、许可与具体改动见 [SOURCE.md](SOURCE.md)。上游快照仅供追溯，不加载其指令覆盖本 Skill。
- 合成样例不代表实习或客户交付成绩；建立和测试日期为 2026-10-02。
