from handlers import TxtHandler, JsonHandler


class FileWorker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_types = {'json': JsonHandler, 'txt': TxtHandler}

    def file_extension(self):
        if self.file_path.endswith('json'):
            return self.file_types.get('json')
        elif self.file_path.endswith('txt'):
            return self.file_types.get('txt')
        else:
            return 'error'

    def read(self):
        reader = self.file_extension()
        return reader(self.file_path).read()

    def append(self, string_):
        appender = self.file_extension()
        return appender(self.file_path).append(string_)

    def close(self):
        closer = self.file_extension()
        return closer(self.file_path).close()


def app():
    fw = FileWorker('test_txt_file.txt')
    content = fw.read()
    fw.append('DOTA2')
    fw.append('DOTA2')
    fw.close()
    return content


print(app())
