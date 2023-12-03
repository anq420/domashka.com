class Moving:
    def move(self):
        raise NotImplementedError


class Animal(Moving):
    def voice(self):
        raise NotImplementedError


class Transport(Moving):
    def launch(self):
        raise NotImplementedError


class Car(Transport):
    def __init__(self):
        self.status = 'not started'

    def move(self):
        if self.status == 'not started':
            print('I am waiting to start engine to start moving')
        if self.status == 'started':
            print('I am moving')

    def launch(self):
        if self.status == 'not started':
            self.status = 'started'
            print(self.status)


class Tiger(Animal):
    def move(self):
        print('It is running')

    def voice(self):
        print('It is roaring')


class Duck(Animal):
    def move(self):
        print('It is swimming')

    def voice(self):
        print('It is quacking')


car = Car()
car.move()
