class Singleton:

    objekt = None

    def __init__(self):
        self.meno = "DB"
        self.heslo = "123456"
        self.ip = "127.0.0.1"
        self.port = 3306

    def pripojDB(self):
        print("pripojenie na databazu")

    @staticmethod
    def getInstance():
        if Singleton.objekt is None:
            obj = Singleton()
            obj.pripojDB()
            Singleton.objekt = obj
        return Singleton.objekt


object1 = Singleton().getInstance()
print(object1.ip)

object2 = Singleton().getInstance()
print(object2.ip)

object3 = Singleton().getInstance()
print(object3.ip)

ZapisDoSuboru.zapis("asdadas")