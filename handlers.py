import json


class BaseHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = None
        self.file = None

    def read(self):
        return NotImplementedError

    def append(self, string_):
        return NotImplementedError

    def close(self):
        return NotImplementedError


class JsonHandler(BaseHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read(self):
        self.file = open(self.file_path, 'r')
        self.content = json.load(self.file)
        if type(self.content) is list:
            print(self.content)
            return self.content
        else:
            return '.json-file must consist of list - []'

    def append(self, string_):
        self.file = open(self.file_path, 'r')
        self.content = json.load(self.file)
        self.content.append(string_)
        with open(self.file_path, 'w') as w_file:
            return json.dump(self.content, w_file)

    def close(self):
        self.file = open(self.file_path, 'r')
        self.file.close()


class TxtHandler(BaseHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read(self):
        self.file = open(self.file_path, 'r')
        self.content = self.file.read()
        return self.content

    def append(self, string_):
        self.file = open(self.file_path, 'a')
        return self.file.write(f'{string_}\n')

    def close(self):
        self.file = open(self.file_path, 'r')
        self.file.close()
