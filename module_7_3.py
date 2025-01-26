import string


class WordsFinder:
    def __init__(self, *file_names): # Сохраняем названия файлов в виде кортежа
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                contents = file.read() # Читаем содержимое файла
                contents = contents.lower() # Переводим содержимое в нижний регистр
                contents = contents.translate(str.maketrans('', '', string.punctuation)) # Убираем пунктуацию
                words = contents.split() # Разбиваем текст на слова
                all_words[file_name] = words  # Сохраняем слова в словаре

        return all_words

    def find(self, word):
        word = word.lower()  # Игнорируем регистр  
        results = {}

        # Используем метод get_all_words для получения слов  
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                # Находим позицию первого вхождения  
                position = words.index(word) + 1  # +1 для 1-индексации  
                results[file_name] = position

        return results

    def count(self, word):
        word = word.lower()  # Игнорируем регистр  
        results = {}

        # Используем метод get_all_words для получения слов  
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            # Считаем количество вхождений слова  
            occurrences = words.count(word)
            if occurrences > 0:
                results[file_name] = occurrences

        return results

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего