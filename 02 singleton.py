# SINGLETON
#
# zabezpečuje, že trieda má len jednu inštanciu, a poskytuje k nej globálny prístupový bod.
# Použitie napríklad na prístup k DB alebo configom.

class Singleton:
    # class variable, zdieľaná medzi všetkými objektmi triedy
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Táto trieda je už bola inštancovaná!")
        else:
            self.meno = "Patrik"
            Singleton._instance = self

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance


s1 = Singleton.getInstance()
print(s1.meno)

s2 = Singleton.getInstance()
s1.meno = "Ivan"
print(s2.meno)
