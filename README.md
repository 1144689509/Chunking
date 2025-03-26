
# 文本分块（Text Chunking）研究项目

## 项目背景

本项目基于 CoNLL-2000 共享任务，专注于文本分块（Text Chunking）技术研究。文本分块是自然语言处理中的一项重要技术，目标是将文本划分为语法相关的词组单元。

## 数据集说明

### 数据来源
- **语料库**：Wall Street Journal (WSJ) 语料库
- **训练数据**：WSJ 语料库第 15-18 节（211,727 个标记）
- **测试数据**：WSJ 语料库第 20 节（47,377 个标记）
- **数据标注**：由蒂尔堡大学 Sabine Buchholz 编写的程序生成

## 技术方法

### 文本分块核心概念
- 将文本划分为语法相关的词组单元
- 识别不同类型的词块，如：
  - NP (名词短语)
  - VP (动词短语)
  - PP (介词短语)
  - ADJP (形容词短语)
  - ADVP (副词短语)

### 标记方法
- B-CHUNK：词块的首个词
- I-CHUNK：词块中的其他词
- O：不属于任何词块的词

## 性能评估

### 评估指标
- F值：精确率和召回率的调和平均数
- 公式：F = 2 * 精确率 * 召回率 / (精确率 + 召回率)

### 基线性能
- 基线F值：77.07%
- 最佳系统F值：94.29%（[ZDJ01]）

## 关键参考文献

1. Abney, S. (1991). Parsing By Chunks.
2. Ramshaw, L. A., & Marcus, M. P. (1995). Text Chunking Using Transformation-Based Learning.
3. Tjong Kim Sang, E. F., & Buchholz, S. (2000). Introduction to the CoNLL-2000 Shared Task: Chunking.

## 相关资源

- [CoNLL-2000 官方网站](https://www.clips.uantwerpen.be/conll2000/)
- [训练数据集](https://www.clips.uantwerpen.be/conll2000/chunking/train.txt.gz)
- [测试数据集](https://www.clips.uantwerpen.be/conll2000/chunking/test.txt.gz)

## 许可

项目中的数据和代码遵循原始语料库和研究论文的使用许可。

---

*最后更新：2025年3月26日*
