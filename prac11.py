class Laptop:
    
    ram_options = {

        4:0,
        8:50,
        16:100,
        32:200,
    }
    disk_space ={

        256:0,
        512:30,
        1024:100,
    }


    def __init__(self,brand,base_price):
        self.brand = brand
        self.base_price = base_price
        self._ram = 4
        self._ssd= 256
    @property
    def ram(self):
        return self._ram
    @ram.setter
    def ram(self,new_ram):
        if new_ram in self.ram_options:
            self._ram = new_ram
    @property
    def ssd(self):
        return self._ssd
    @ssd.setter
    def ssd(self,new_ssd):
        if new_ssd in self.disk_space:
            self._ssd = new_ssd

    def calculate(self):
        ram_price  = self.ram_options[self.ram]
        total_price = self.base_price + ram_price
        return total_price

    def __str__(self):
        output = f"{self.brand} laptop with {self.ram} gb ram"
        output += f" priced at {self.calculate()}"
        output += f" has {self.ssd} space" 
        return output

class ShoppingCart:
    def __init__(self):
        self.laptops = []
        self.total = 0
    
    def add_laptops(self,laptop):
        self.laptops.append(laptop)
        laptop_price = laptop.calculate()
        self.total += laptop_price

    def __str__(self):
        output = "shopping cart contains \n"
        for laptop in self.laptops:
            output += f"{laptop} \n"
        output += f"total price {self.total}"
        return output

class GamingLaptop(Laptop):
    gpu_options ={
    
        "NVIDIA GTX 1650":0,
        "NVIDIA RTX 3070":250,
        "NVIDIA RTX 4080":350,
        "AMD RX 6800M":280,

    }
    def __init__(self,brand,base_price):
        super().__init__(brand,base_price)
        self._gpu = "NVIDIA GTX 1650"
    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self,new_gpu):
        if new_gpu in self.gpu_options:
            self._gpu = new_gpu
    def calculate(self):
        gpu_price = self.gpu_options[self.gpu]
        laptop_price = super().calculate()
        total_price = laptop_price + gpu_price
        return total_price
    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} Gb ram"
        output += f" and {self.gpu} priced at {self.calculate()}"
        return output



def test_laptop():
    gaming = GamingLaptop("Razer",2399.99)
    print(gaming)


def test_shop():
    cart = ShoppingCart()
    dell = Laptop("dell",999.99)
    hp = Laptop("hp",1349.00)
    cart.add_laptops(dell)
    cart.add_laptops(hp)
    print(cart.total)
    print(cart)

def test():
    laptop = Laptop("Dell",999.99)
    print(laptop.brand)
    print(laptop.ram)
    laptop.ram = 16
    print(laptop.ram)
    print(laptop.base_price)
    print(laptop.calculate())
    print(laptop)
    laptop.ssd = 512
    print(laptop)

test()
