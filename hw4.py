import math

class CountVectorizer:
    def init(self):
        """создаёт для объекта класса словарь и матрицу, которую будет возвращать"""
        self.dict = {}
        self.matrix = []

    def dict_transformer(self, texts):
        """Преобразует все слова в переданном массиве и запоминает номера добавления новых элементов"""
        schet = 0
        for string in texts:
            string = string.lower().split()
            for word in string:
                if word not in self.dict:
                    self.dict[word] = 1
                else:
                    self.dict[word] += 1

    def  fit_transform(self, texts: list) -> list:
        """Фунцкия смотрит на каждое слово в отдельной строке и добавляет 1 на то место,
        в котором слово было добавлено в словарь. Так же для каждого отдельного вызова
        fit_transform нужно очистить словарь и терм-документную матрицу"""
        self.dict = {}
        self.matrix = []
        self.dict_transformer(texts)
        a = sum(list(self.dict.values()))
        for string in texts:
            matrix_row = [0 for i in range(len(self.dict))]
            string = string.lower().split()
            for ind, word in enumerate(self.dict.values()):
                matrix_row[ind] = round(word / a, 3)
            self.matrix.append(matrix_row)
        return self.matrix

    def get_feature_names(self, *texts) -> list:
        """Если self.dict не пустой, значит функция dict_transformer уже была вызвана
        и нам не нужно её вызывать снова, а если пустой, то значит мы не применяли функцию
        fit_transform"""
        if self.dict == {}:
            self.dict_transformer(texts[0])
        return list(self.dict.keys())


class TfidfTransformer():
    def tf_transform(self, count_matrix):
        tf_matrix = []
        for rows in count_matrix:
            lenght = sum(rows)
            row = []
            for freq in rows:
                row.append((freq / lenght))
            tf_matrix.append(row)

        return tf_matrix

    def idf_transform(self, count_matrix):
        d = {}
        if count_matrix[0] == 1:
            return [1 for i in range(len(count_matrix))]

        for i in range(len(count_matrix[0])):
            frq = 0
            for j in range(len(count_matrix)):
                if count_matrix[j][i] != 0:
                    frq += 1
            d[i] = frq

        idf_matrix = [(math.log((len(count_matrix) + 1) / (d[i] + 1))) + 1 for i in range(len(count_matrix[0]))]
        return idf_matrix

    def fit_transform(self, count_matrix) -> list:
        idf = self.idf_transform(count_matrix)
        tf = self.tf_transform(count_matrix)

        tfidf = [[round(t*i,3) for t, i in zip(tf_row, idf)] for tf_row in tf]
        return tfidf


class TfidfVectorizer(CountVectorizer):
    def init(self):
        super().init()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, data: list) -> list:
        count_matrix = super().fit_transform(data)
        return self.tf_idf_transformer.fit_transform(count_matrix)

count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(count_matrix)
print(tfidf_matrix)