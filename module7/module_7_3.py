class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower().strip()
                    line = line.replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace(' - ', ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result
        