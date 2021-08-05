class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def greeting(self):
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))