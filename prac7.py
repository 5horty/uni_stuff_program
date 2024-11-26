from graphix import Window,Circle,Rectangle,Point,Text,Entry,Polygon
from prac5 import distance_between_points,draw_brown_eye

import time

def hello_while():
    i = 0
    while i < 10:
        print("i is now", i)
        i = i + 1


def countdown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


def mystery_loop():
    i = 1
    # Be careful! This loop will run forever!
    while i < 1000:
        print(i)
        i = i * 2


def add_up_numbers1():
    total = 0
    more_numbers = "y"
    while more_numbers == "y":
        number = int(input("Enter a number: "))
        total = total + number
        more_numbers = input("Any more numbers? (y/n) ")
    print("The total is", total)


def add_up_numbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def add_up_numbers3():
    total = 0
    n_str = input("Number (hit enter to stop): ")
    while n_str != "":
        number = int(n_str)
        total += number
        n_str = input("Number (hit enter to stop): ")
    print("The total is", total)


def add_up_numbers4():
    total = 0
    while True:
        n_str = input("Number (anything else to stop): ")
        if not n_str.isdigit():
            break  # Exit the loop if the input is not a number
        number = int(n_str)
        total += number
    print("The total is", total)


# Note: msg == "" needs to appear twice
def get_string1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def get_string2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def can_apply_for_job(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False


def can_vote1():
    age = int(input("How old are you? "))
    while age <= 18:
        print("Wait until you are 18!")
        age = int(input("How old are you? "))


def can_vote2():
    while True:
        age = int(input("How old are you? "))
        if age > 18:
            break
        print("Wait until you are 18!")


#  For question 2
def traffic_lights():
    win = Window()
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    while True:
        red.fill_colour = "red"
        time.sleep(1)
        amber.fill_colour = "yellow"
        time.sleep(1)
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        time.sleep(1)
        green.fill_colour="black"
        amber.fill_colour ="yellow"
        time.sleep(1)
        amber.fill_colour ="black"
   

        # remove the `pass` and add your code here


# For question 6
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32



def get_name():
    name = input("enter your name: ")
    while not name.isalpha():
        name = input("invalid name \nenter your name: ")
    return name


   



        
        
def cal_grade():
    mark = int(input("enter a mark "))
    grades = ["A","B","C","F"]
    flag = True
    while flag:
        if 16 <= mark <= 20:
            return grades[0]
        elif 12 <= mark <= 15:
            return  grades[1]
        elif 8 <= mark <= 11:
            return grades[2]
        elif 0 <= mark < 8:
            return grades[3]
        else:
            mark = int(input("mark invalid \nenter a mark "))



def order_price():
    total = 0
    more = "yes"
    while more:
        money = float(input("enter a price: "))
        quant = int(input("enter number of items: "))
        man = money * quant
        total+= man
        more = input("are there more (leave blank if no) ")
    print(f"here is the total {total:.2f}")


def clickable_eye():
    win = Window("",400,400)
    center = Point(100,100)
    flag = True
    rad = 100
    text = Text(Point(200,350),"")
    draw_brown_eye(win,center,rad)
    text.draw(win)
    while True:
        click = win.get_mouse()
        diff = distance_between_points(click,center)
        if diff <= 25:
            text.text = "pupil"
        elif diff <= 50:
            text.text = "iris"
        elif diff <= 100:
            text.text = "white"
        else:
            win.close()

        

