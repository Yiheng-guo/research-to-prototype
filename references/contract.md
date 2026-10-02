# 输入、运行与验收

从 Skill 目录运行：

```bash
python3 scripts/run.py examples/input.json --output /tmp/research-to-prototype-output.json
python3 scripts/run.py examples/failure-input.json --output /tmp/research-to-prototype-failure.json
```

根字段：version、evidence、requirements、changes。完整字段、数组与枚举见 [input.json](../examples/input.json)。支持Python 3.9+，无需第三方包和API。输出路径必须不存在。语义判断不是脚本自动推理。

验证重点与回退：未知证据E999引用被拒绝；回退到证据采集，不凭空加证据。

成功状态按任务区分：ready_for_human_review/ready_for_visual_review 表示等待内容审核；draft_requires_clarification 表示未承诺范围；proposal_only 表示未写平台记忆。blocked/failed 返回2；普通运行错误也返回2。成功退出不代表生产验收。
