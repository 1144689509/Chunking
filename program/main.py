import os
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression


class ChunkParser:
    def __init__(self):
        self.vectorizer = DictVectorizer(sparse=True)  # 使用稀疏矩阵，减少内存占用
        self.classifier = LogisticRegression(multi_class='ovr', max_iter=1000, solver='saga', n_jobs=-1)

    def load_conll_data(self, filename):
        sentences = []
        current_sentence = []

        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    if current_sentence:
                        sentences.append(current_sentence)
                        current_sentence = []
                else:
                    parts = line.split()
                    if len(parts) >= 3:
                        word, pos, chunk = parts[0], parts[1], parts[2]
                        current_sentence.append((word, pos, chunk))

        if current_sentence:
            sentences.append(current_sentence)

        return sentences

    def extract_features(self, sentence, index):
        features = {
            'word': sentence[index][0].lower(),  # 统一为小写，减少维度
            'pos': sentence[index][1]
        }

        if index > 0:
            features['prev_word'] = sentence[index - 1][0].lower()
            features['prev_pos'] = sentence[index - 1][1]

        if index < len(sentence) - 1:
            features['next_word'] = sentence[index + 1][0].lower()
            features['next_pos'] = sentence[index + 1][1]

        return features

    def prepare_data(self, tagged_sentences):
        X = []
        y = []

        for sentence in tagged_sentences:
            for i in range(len(sentence)):
                features = self.extract_features(sentence, i)
                label = sentence[i][2]
                X.append(features)
                y.append(label)

        return X, y

    def train(self, train_file):
        train_sentences = self.load_conll_data(train_file)
        X, y = self.prepare_data(train_sentences)

        X_vectorized = self.vectorizer.fit_transform(X)  # 使用稀疏矩阵
        self.classifier.fit(X_vectorized, y)

    def predict(self, sentence):
        features = [self.extract_features(sentence, i) for i in range(len(sentence))]
        X_vectorized = self.vectorizer.transform(features)
        predictions = self.classifier.predict(X_vectorized)

        return list(zip(sentence, predictions))

    def evaluate(self, test_file):
        test_sentences = self.load_conll_data(test_file)
        X_test, y_true = self.prepare_data(test_sentences)

        X_test_vectorized = self.vectorizer.transform(X_test)
        y_pred = self.classifier.predict(X_test_vectorized)

        accuracy = sum(y_p == y_t for y_p, y_t in zip(y_pred, y_true)) / len(y_true)

        from sklearn.metrics import classification_report
        print("分类报告：")
        print(classification_report(y_true, y_pred))

        return accuracy


def main():
    train_file = 'train.txt'
    test_file = 'test.txt'

    if not os.path.exists(train_file):
        print(f"错误：未找到训练文件 {train_file}")
        return

    if not os.path.exists(test_file):
        print(f"错误：未找到测试文件 {test_file}")
        return

    chunk_parser = ChunkParser()

    print("正在训练模型...")
    chunk_parser.train(train_file)

    print("\n正在评估模型...")
    accuracy = chunk_parser.evaluate(test_file)
    print(f"\n模型准确率: {accuracy:.2%}")

    print("\n示例预测：")
    test_sentences = chunk_parser.load_conll_data(test_file)
    if test_sentences:
        example_sentence = [(word, pos) for word, pos, _ in test_sentences[0]]
        result = chunk_parser.predict(example_sentence)

        print("测试句子：", example_sentence)
        print("词块预测：")
        for (word, pos), chunk_tag in result:
            print(f"{word}/{pos}: {chunk_tag}")


if __name__ == '__main__':
    main()
