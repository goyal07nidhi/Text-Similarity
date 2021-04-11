import string


class TextSimilarity():
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def get_stopwords(self) -> list:
        stopwords = list()
        with open("stopwords.txt", "r") as stop_file:
            stopwords = stop_file.read().replace('\n', '')

        return stopwords

    def pre_process(self, text: str) -> list:
        stopwords = self.get_stopwords()

        # 1. Remove stop words
        tokens = text.split()
        tokens = [word.lower() for word in tokens if word.lower() not in stopwords]

        # 2. Remove punctuation
        tokens = [word.translate(str.maketrans('', '', string.punctuation)) for word in tokens]

        return tokens

    def generate_ngram(self, tokens: list, ngram_len: int) -> list:
        if ngram_len < 1:
            return list()
        return list(zip(*[tokens[ngram_len-1:]]))

    def calculate_score(self, ngram_len: int) -> float:
        # 1. preprocess
        token1 = self.pre_process(self.text1)
        token2 = self.pre_process(self.text2)

        if token1 == token2:
            return 1.0

        # 2. generate ngram
        ngram1 = self.generate_ngram(token1, ngram_len)
        ngram2 = self.generate_ngram(token2, ngram_len)

        # 3. calculate score
        num_unique_ngram = len(set(ngram1 + ngram2))
        num_common_ngram = len(set([ngram for ngram in ngram1 if ngram in ngram2]))

        if num_unique_ngram == 0:
            return 0.0

        return round(num_common_ngram / num_unique_ngram, 2)
