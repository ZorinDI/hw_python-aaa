class CountVectorizer:
    def __init__(self):
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
                    self.dict[word] = schet
                    schet += 1


    def fit_transform(self, texts: list) -> list:
        """Фунцкия смотрит на каждое слово в отдельной строке и добавляет 1 на то место,
        в котором слово было добавлено в словарь"""
        self.dict_transformer(texts)
        for string in texts:
            matrix_row = [0 for i in range(len(self.dict))]
            string = string.lower().split()
            for word in string:
                matrix_row[self.dict[word]] += 1
            self.matrix.append(matrix_row)
        return self.matrix

    def get_feature_names(self, *texts) -> list:
        """Если self.dict не пустой, значит функция dict_transformer уже была вызвана
        и нам не нужно её вызывать снова, а если пустой, то значит мы не применяли функцию
        fit_transform"""
        if self.dict == {}:
            self.dict_transformer(texts[0])
        return list(self.dict.keys())
