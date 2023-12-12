from handlers import TxtHandler, JsonHandler
from exception import ExtensionError


class FileWorker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.extension = self.file_extension()

    def file_extension(self):
        file_types = {'json': JsonHandler, 'txt': TxtHandler}
        extension = self.file_path.split('.')[-1]
        if extension in file_types:
            get_handler = file_types.get(extension)
            return get_handler(self.file_path)
        else:
            raise ExtensionError('Unsupported file extension')

    def read(self):
        return self.extension.read()

    def append(self, content):
        return self.extension.append(content)

    def close(self):
        return self.extension.close()


def app():
    fw = FileWorker('file.json')
    content = fw.read()
    fw.append('DOTA2')
    fw.append('DOTA2')
    fw.close()
    return content


app()
