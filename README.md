
# 文本分块（Text Chunking）机器学习项目

## 项目概述

本项目实现了一个基于机器学习的文本分块（Text Chunking）系统，使用逻辑回归分类器从CoNLL-2000数据集中学习识别文本中的语法词组。

## 项目架构

### 主要模块功能

#### `ChunkParser` 类

1. **`__init__` 方法**
   - 初始化特征向量化器和逻辑回归分类器
   - 使用稀疏矩阵优化内存占用
   - 配置多分类逻辑回归模型

2. **`load_conll_data` 方法**
   - 加载CoNLL格式的文本数据
   - 解析每个句子的单词、词性标注和词块标签
   - 处理换行和空行，确保正确分割句子

3. **`extract_features` 方法**
   - 从单词周围的上下文提取特征
   - 提取特征包括：
     - 当前单词（小写）
     - 当前词性标签
     - 前一个单词（小写）
     - 前一个词性标签
     - 后一个单词（小写）
     - 后一个词性标签

4. **`prepare_data` 方法**
   - 将标注好的句子转换为机器学习可用的格式
   - 生成特征矩阵和标签列表

5. **`train` 方法**
   - 加载训练数据
   - 特征向量化
   - 训练逻辑回归分类器

6. **`predict` 方法**
   - 对新句子进行词块预测
   - 返回每个单词的预测词块标签

7. **`evaluate` 方法**
   - 加载测试数据
   - 计算模型准确率
   - 生成详细的分类报告

## 词块类型

### CoNLL-2000 数据集支持的词块类型

1. **NP (名词短语)**
   - 包含名词及其修饰语
   - 示例：the big dog, my nice car

2. **VP (动词短语)**
   - 包含动词及其补语、状语
   - 示例：is running, will go home

3. **PP (介词短语)**
   - 以介词开头的短语
   - 示例：in the house, after the meeting

4. **ADVP (副词短语)**
   - 由副词及其修饰语组成
   - 示例：very quickly, quite well

5. **ADJP (形容词短语)**
   - 包含形容词及其修饰语
   - 示例：extremely happy, quite smart

### 词块标签详解

- **B-CHUNK**: 词块的第一个词（Begin）
- **I-CHUNK**: 词块中的其他词（Inside）
- **O**: 不属于任何词块的词（Outside）

## 依赖库

- scikit-learn
- os

## 使用方法

1. 准备CoNLL格式的训练和测试数据集
2. 运行 `main()` 函数
3. 查看模型训练结果和评估指标

## 性能指标

- 使用逻辑回归多分类
- 全面评估指标：准确率、召回率、F1分数

## 参考文献

1. Abney, S. (1991). Parsing By Chunks.
2. Ramshaw, L. A., & Marcus, M. P. (1995). Text Chunking Using Transformation-Based Learning.
3. Tjong Kim Sang, E. F., & Buchholz, S. (2000). Introduction to the CoNLL-2000 Shared Task: Chunking.

## 许可

MIT 开源许可

---

*最后更新：2025年3月26日*
