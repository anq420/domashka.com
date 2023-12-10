from handlers import TxtHandler, JsonHandler


class FileWorker:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_extension(self):
        if self.file_path.endswith('.json'):
            return '.json'
        elif self.file_path.endswith('.txt'):
            return '.txt'

    def read(self):
        if self.file_extension() == '.json':
            return JsonHandler(self.file_path).read()
        if self.file_extension() == '.txt':
            return TxtHandler(self.file_path).read()

    def append(self, string_):
        if self.file_extension() == '.json':
            return JsonHandler(self.file_path).append(string_)
        if self.file_extension() == '.txt':
            return TxtHandler(self.file_path).append(string_)

    def close(self):
        if self.file_extension() == '.json':
            return JsonHandler(self.file_path).close()
        if self.file_extension() == '.txt':
            return TxtHandler(self.file_path).close()


def app():
    fw = FileWorker('test_txt_file.txt')
    content = fw.read()
    fw.append('DOTA2')
    fw.append('DOTA2')
    fw.close()
    return content


print(app())
