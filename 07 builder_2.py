class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.color = None
        self.power = None
        self.case_brand = None

    def add_cpu(self, cpu):
        self.cpu = cpu

    def add_gpu(self, gpu):
        self.gpu = gpu

    def add_ram(self, ram):
        self.ram = ram

    def add_storage(self, storage):
        self.storage = storage

    def add_color(self, color):
        self.color = color

    def add_power(self, power):
        self.power = power

    def add_case_brand(self, case_brand):
        self.case_brand = case_brand


computer1 = Computer(
    cpu='Intel',
    gpu='Nvidia',
    ram='16GB',
    storage='1TB',
    color='Black',
    power='15W',
    case_brand='Asus'
)

computer2 = Computer(
    cpu='AMD',
    gpu='Nvidia',
    ram='8GB',
    storage='500GB',
    color='White',
    power='10W',
    case_brand='Gigabyte'
)

# verzia2:
class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.color = None
        self.power = None
        self.case_brand = None

    def add_cpu(self, cpu):
        self.cpu = cpu

    def add_gpu(self, gpu):
        self.gpu = gpu

    def add_ram(self, ram):
        self.ram = ram

    def add_storage(self, storage):
        self.storage = storage

    def add_color(self, color):
        self.color = color

    def add_power(self, power):
        self.power = power

    def add_case_brand(self, case_brand):
        self.case_brand = case_brand

    def build(self):
        return Computer(
            self.cpu,
            self.gpu,
            self.ram,
            self.storage,
            self.color,
            self.power,
            self.case_brand
        )


computer1 = Computer(
    cpu='Intel',
    gpu='Nvidia',
    ram='16GB',
    storage='1TB',
    color='Black',
    power='15W',
    case_brand='Asus'
)

computer2 = Computer(
    cpu='AMD',
    gpu='Nvidia',
    ram='8GB',
    storage='500GB',
    color='White',
    power='10W',
    case_brand='Gigabyte'
)

computerBuilder = ComputerBuilder()
computerBuilder.add_storage("2TB")
computerBuilder.add_ram("32GB")
computerBuilder.add_power("20W")

computer3 = computerBuilder.build()

computer4 = Computer(cpu=None, gpu=None, ram=None, storage="32GB")

print(computer3)