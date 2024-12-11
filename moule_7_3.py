class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = file_name

    def get_all_words(self):
        all_words = {}

        for filename in self.file_names:
            with open(filename, encoding='utf-8') as f:
                content = f.read()

            # Приведение к нижнему регистру
            content_lower = content.lower()

            # Удаление знаков препинания
            punctuation = [',', '.', '=', '!', '?', ';', ':', '-', '(', ')']
            for punc in punctuation:
                content_lower = content_lower.replace(punc, '')

            # Разбиение строки на слова
            words = content_lower.split()

            # Добавление слов в словарь
            all_words[filename] = words

        return all_words

    def find(self, word):
        result = {}
        all_words_dict = self.get_all_words()

        for filename, words in all_words_dict.items():
            try:
                index = words.index(word.lower())
                result[filename] = index + 1
            except ValueError:
                pass

        return result

    def count(self, word):
        result = {}
        all_words_dict = self.get_all_words()

        for filename, words in all_words_dict.items():
            count_word = words.count(word.lower())
            if count_word > 0:
                result[filename] = count_word

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
