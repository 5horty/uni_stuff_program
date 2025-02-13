from graphix import Point, Window, Rectangle, Circle, Line

class MyPoint():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"


class Square():
    def __init__(self,p1,side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.x + side, p1.y + side)
        self.outline_colour = "black"
        self.fill_colour = "white"
    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)
    
    def perimeter(self):
        return self.side*4

    def area(self):
        return self.side*self.side
    def center(self):
        return MyPoint((self.p1.x+self.p2.x)//2,(self.p1.y+self.p2.y)//2)

    def __str__(self):
        return f"Square({self.p1}, {self.p2})"

class MyCircle():
    def __init__(self,center,rad):
        self.center = center
        self.rad = rad
        self.fill_colour = "white"
        self.outline_colour = "black"
    def move(self,dx,dy):
        self.center.move(dx,dy)
    def __str__(self):
        return f"Circle({self.center}, {self.rad})"

class BankAccount():
    def __init__(self,name,):
        self.name = name
        self.money = 0
    def deposit(self,amount):
        self.money += amount
    def withdraw(self,amount):
        self.money -= amount
    def __str__(self):
        return f" bank account for {self.name} has {self.money}"

class HotelRoom():
    def __init__(self,room_num):
        self.room_num = room_num
        self.guest_name = ""
    def check_in(self,guest_name):
        self.guest_name= guest_name
    def check_out(self):
        self.guest_name = ""
    def is_occupied(self):
        if self.guest_name:
            return f" room {self.room_num} is occipied by {self.guest_name}"
        else:
            return f" room {self.room_num} is empty"
    

class GradeBook():
    def __init__(self,):
        self.grades ={}
    def add_grade(self,name,grade):
        if name not in grades.keys():
            self.grades[name] = grade
        else:
            return "already in the list"
    def remove_grade(self,name):
        if name in grades.keys():
            self.grades.pop(name)
        else:
            return "grade not in grades"
    def average(self):
        x = 0
        for i in self.grades.values():
            x+= i
        return x//len(self.grades.values())
    def __str__(self):
        if self.grades:
            return f"{self.grades}"
        else:
            return f"empty"

def testgrade():
    stu = GradeBook()
    print(stu)

class Smartphone():
    def __init__(self,colour,memory):
        self.colour = colour
        self.memory = memory
        self.apps = ["Phone","Messages","Camera"]
        self.current = self.apps[0] 
    def install_apps(self,name):
        self.apps.append(name)
        print(f"installing {name} app ... \n")
    def choose_app(self,name):
        if name in self.apps:
            self.current = name
    def __str__(self):
        output = ""
        for i in self.apps:
            if i == self.current:
                output += (i + "  current"+ "\n")
            else:
                output += (i + "\n")
        return output



            


def testphone():
    p = Smartphone("Black" , 128)
    p.choose_app("Messages")
    p.install_apps("discord")
    p.choose_app("discord")
    print(p)

testphone()




def testhotel():
    room_101 = HotelRoom(101)
    room_101.guest_name = "rogna"
    print(room_101.is_occupied())
    room_101.guest_name = ""
    print(room_101.is_occupied())



def test_bank():
    bank = BankAccount("rogan macleod")
    print(bank)
    bank.deposit(100)
    print(bank)
    bank.withdraw(50)
    print(bank)


def test_square():
    p = MyPoint(100, 50)
    square = Square(p, 50)

    print("square's side length is", square.side)  # 50
    print("square's p1 is", square.p1)  # MyPoint(100, 50)
    print("square's p2 is", square.p2)  # MyPoint(150, 100)

    square.side = 100
    print("After changing square's side length to 100 ...")
    print("square's side length is", square.side)  # 100
    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.side)  # 100
    print("square's p1 is", square.p1)  # MyPoint(110, 30)
    print("square's p2 is", square.p2)  # MyPoint(160, 80)
    print(square)
    print(square.outline_colour)
    print(square.fill_colour)
    square.outline_colour = "purple"
    square.fill_colour= "yellow"
    print(square.outline_colour)
    print(square.fill_colour)
    prints(quare.perimeter())
    print(square.area())
    print(square.center())
#test_square()

def test_circle():
    c = MyCircle(MyPoint(100,200),50)
    c.move(10,-10)
    print(c)

    
#test_circle()

def test_my_point():
    my_point = MyPoint(100, 50)
    print("my_point's x coordinate is", my_point.x)  # 100
    print("my_point's y coordinate is", my_point.y)  # 50
    my_point.move(10, -20)
    print("my_point's x coordinate is", my_point.x)  # 110
    print("my_point's y coordinate is", my_point.y)  # 30

#test_my_point()

def test_point():
    p = Point(100, 50)
    print("p is of type:", type(p))  # <class 'graphix.Point'>
    print("p's x coordinate is", p.x)  # 100
    print("p's y coordinate is", p.y)  # 50

    p.move(10, -20)
    print("p's x coordinate is", p.x)  # 110
    print("p's y coordinate is", p.y)  # 30

    print("p is:", p)  # p is: Point(110, 30)


#test_point()
