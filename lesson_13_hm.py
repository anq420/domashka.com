import json


class DataStorage:
    def __init__(self, file_path):
        self.status = 'disconnect'
        self.content = None
        self._file_path = file_path

    def _create_storage(self):
        with open(self._file_path, 'w') as j_file:
            json.dump([], j_file)

    def connect(self):
        try:
            with open(self._file_path, 'r') as j_file:
                self.content = json.load(j_file)
                self.status = 'connected'
        except FileNotFoundError:
            return self._create_storage()

    def disconnect(self):
        if self.status == 'connected':
            self.status = 'disconnected'
            print('The file was closed')


class DataStorageWrite(DataStorage):
    def connect(self):
        try:
            with open(self._file_path, 'r') as j_file:
                self.content = json.load(j_file)
                self.status = 'connected'
        except FileNotFoundError:
            return self._create_storage()

    def append(self, string_):
        if self.status == 'connected':
            self.content.append(string_)
            with open(self._file_path, 'w') as j_file:
                json.dump(self.content, j_file)
        else:
            print('You need to set a "connect" status first')


file = DataStorage('file.json')
file._create_storage()
file.connect()
file.disconnect()
print(file.content)

file_1 = DataStorageWrite('file.json')
file_1.append('Hello, world')
file_1.disconnect()
print(file_1.content)
