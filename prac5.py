import math
from graphix import Window, Circle, Point, Entry, Text


def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divide_and_product(a, b):
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result


def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product_result, divide_result = divide_and_product(num1, num2)
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")


def calc_future_value(amount, years):
    interest_rate = 0.065
    for year in range(years):
        amount = amount * (1 + interest_rate)
    return amount


def future_value():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# For exercises 1 and 2
def area_of_circle(radius):
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    return (2 * math.pi) * radius


def circle_info():
    area = int(input("enter a number "))
    rad = int(input("enter a number "))
    area_real =area_of_circle(area)
    circum = circumference_of_circle(rad)
    print(f"here is the area {area_real:.3f} and circum {circum:.3f}")







# For exercise 3
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


def draw_brown_eye_in_centre():
    window = Window()
    # Add your code here
    center = Point(200,200)
    draw_circle(window,center,120,"white")
    draw_circle(window,center,60,"white")
    draw_circle(window,center,30,"brown")

    window.get_mouse()
    window.close()

def draw_block_of_stars(width,height):
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print()
        

def draw_letter_e():

    draw_block_of_stars(8,2)
    draw_block_of_stars(2,2)
    draw_block_of_stars(5,2)
    draw_block_of_stars(2,2)
    draw_block_of_stars(8,2)








# For exercise 5
def draw_brown_eye(win, centre, radius):
    
    # Remove pass and add your code here
    draw_circle(win,centre,radius,"white")
    draw_circle(win,centre,(radius//2),"brown")
    draw_circle(win,centre,(radius//4),"black")

def draw_pair_of_eyes():
    win = Window()
    cent = Point(200,200)
    draw_brown_eye(win,cent,120)
    win.get_mouse()
    win.close()

def draw_pair_of_brown_eyes():
    win = Window()
    cent_eye_one = Point(100,200)
    draw_brown_eye(win,cent_eye_one,100)
    cent_eye_two = Point(300,200)
    draw_brown_eye(win,cent_eye_two,100)
    win.get_mouse()
    win.close()


def distance_between_points(p1,p2):
    return ((p2.x-p1.x)**2 + (p2.y-p1.y)**2)**0.5


def distance_calc():
    win = Window()

    text = Text(Point(200,30),"click 2 points")
    text.draw(win)
    
    point1 = win.get_mouse()
    point2 = win.get_mouse()

    diff=round(distance_between_points(point1,point2),2)
    diff = str(diff)
    text.text = diff


    win.get_mouse()
    win.close()


def draw_blocks(one,two,three,four,five):
    for i in range(five):
        line = ""

        line += " " * one

        line += "*" * two

        line += " " * three

        line += "*" * four


        print(line)






def draw_letter_a():
    draw_blocks(1,8,0,0,2)
    draw_blocks(0,2,6,2,2)
    draw_blocks(0,10,0,0,2)
    draw_blocks(0,2,6,2,3)

def draw_four_pairs_of_brown_eyes():
    win = Window("",800,800)

    click1 = win.get_mouse()
    click2 = win.get_mouse()


    rad = int(distance_between_points(click1,click2))


    draw_brown_eye(win,click1,rad)
    click1 = Point(click1.x + (rad*2),click1.y)
    draw_brown_eye(win,click1,rad)

    click3 = win.get_mouse()
    click4 = win.get_mouse()

    rad2 = int(distance_between_points(click3,click4))

    draw_brown_eye(win,click3,rad2)
    print(click3.x)
    click3 = Point(click3.x + (rad2*2),click3.y)
    print(click3.x)
    draw_brown_eye(win,click3,rad2)

    win.get_mouse()
    win.close()


def display_text_with_spaces(win,size,pos,text):
    texts  = text.text
    texts = texts.upper()
    #numnew = size.text
    #numnew = int(numnew)
    numnew = size
    newtext = ""
    for char in texts:
        newtext += char+ " "

    textbox = Text(Point(pos.x,pos.y),"")
    textbox.text = newtext
    textbox.size = numnew
    textbox.draw(win)

def test43():
    win = Window("",800,800)
    
    tezt = Entry(Point(200,200),10)
    tezt.draw(win)
    win.get_mouse()
    num = Entry(Point(200,300),10)
    num.draw(win)
    posi = win.get_mouse()
    display_text_with_spaces(win,num,posi,tezt)

    win.get_mouse()
    win.close()

def construct_vision_chart():
    win = Window("",800,700)
    position = Point(400,100)
    textsize = 30
    for i in range(1,7,1):
        text = Entry(Point(200,200),10)
        text.draw(win)
        win.get_mouse()
        display_text_with_spaces(win,textsize,position,text)
        position = Point(400,100+(100*i))
        textsize -= 5

    win.get_mouse()
    win.close()



