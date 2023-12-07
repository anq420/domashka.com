import json


class DataStorage:
    def __init__(self, file_path):
        self.status = 'disconnect'
        self.content = None
        self.__file_path = file_path
        self.file = None

    @property
    def file_path(self):
        return self.__file_path

    def _create_storage(self):
        with open(self.file_path, 'w') as j_file:
            json.dump([], j_file)
            return j_file

    def connect(self):
        try:
            self.file = open(self.file_path, 'r')
            self.content = json.load(self.file)
            self.status = 'connected'
            return self.file
        except FileNotFoundError:
            self._create_storage()
            self.file = open(self.file_path, 'r')
            self.content = json.load(self.file)
            self.status = 'connected'
            return self.file

    def disconnect(self):
        if self.status == 'connected':
            self.file.close()
            self.status = 'disconnected'
            print('The file was closed')


class DataStorageWrite(DataStorage):
    def connect(self):
        super().connect()

    def _create_storage(self):
        super()._create_storage()

    def append(self, string_):
        if self.status == 'connected':
            self.content.append(string_)
            with open(self.file_path, 'w') as j_file:
                json.dump(self.content, j_file)
        else:
            print('You need to set a "connect" status first')


j_file_1 = DataStorageWrite('file.json')
j_file_1.connect()
j_file_1.append('Hello, world')
j_file_1.disconnect()
print(j_file_1.content)
