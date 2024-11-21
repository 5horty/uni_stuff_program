from graphix import Window, Rectangle, Circle, Point, Text, Entry
import math
import random

def fast_food_order_price():
    order = float(input("enter an amount "))
    if order < 20:
        order+=2.50
    print(f"the total price is {order:.2f} ")

def what_to_do_today():
    temp = int(input("enter todays temp "))
    if temp > 25:
        print("swim in the sea")
    elif 10 <= temp <= 25:
        print("shop at gunwharf")
    else:
        print("watch stuff at home")

def display_square_roots(start,end):
    for i in range(start,end+1):
        print(f"the square root of {i} is {math.sqrt(i):.3f}")



def calculate_grade(mark):
    grades = ["A","B","C","F","X"]
    if 16 <= mark <= 20:
        return grades[0]
    elif 12 <= mark <= 15:
        return  grades[1]
    elif 8 <= mark <= 11:
        return grades[2]
    elif 0 <= mark < 8:
        return grades[3]
    else:
        return grades[4]


def peas_in_a_pod():
    num_peas = int(input("enter number a peas "))
    length = num_peas* 100
    win = Window("",length,100)
    dist = 50
    for i in range(1,num_peas+1):
        circ = Circle(Point(dist,50),50)
        dist += 100
        circ.fill_colour = "green"
        circ.draw(win)

    win.get_mouse()
    win.close()

def ticket_price(distance,age):
    tickets = 10.00
    kilo_per = 0.15
    for i in range(distance):
        tickets +=kilo_per

    if age >= 60:
        tickets = tickets - (tickets * 0.4)
    print(f"here is the price {tickets:.2f}")


def numberes_square(n):
    for i in range(n):
        print(n - i,end = " ")
        for j in range(1,n):
            print((n-i)+ j,end=" ")
        print() 


def draw_circle(win,center,rad,colour):
    circle = Circle(center,rad)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


def draw_coloured_eye():
    colur = input("enter a colour ")
    win = Window()
    center = Point(200,200)
    draw_circle(win,center,120,"white")
    draw_circle(win,center,60,colur)
    draw_circle(win,center,30,"black")
    win.get_mouse()
    win.close()

def draw_eye_help(win,point,rad,colour):
    draw_circle(win,point,rad,"white")
    draw_circle(win,point,rad//2,colour)
    draw_circle(win,point,rad//4,"black")

def eye_picker():
    eyes= ["blue","grey","green","brown"]
    rad = int(input("enter a radius "))
    x = int(input("enter the x coordinates"))
    if x > 400:
        print("invalid coordinates ")
    else:
        y = int(input("enter the y coordinates"))
        if y > 400:
            print("coordinates not valid")
        else:
            center = Point(x,y)
            eye_colour = input("enter the eye colour ")
            win = Window()
            for i in range(len(eyes)):
                if eye_colour in eyes:
                    draw_circle(win,center,rad,"white")
                    draw_circle(win,center,(rad//2),eye_colour)
                    draw_circle(win,center,(rad//4),"black")
                    win.get_mouse()
                    win.close()
                else:
                    print("invalid eye colour ")
                    break


def rectangle(win,point1,point2,colour,out_colur):
    rect = Rectangle(point1,point2)
    rect.fill_colour = colour
    rect.outline_colour = out_colur
    rect.draw(win)

def text(win,point1,texts,size):
    textz = Text(point1,texts)
    textz.fill_colour = "red"
    textz.size = size
    textz.draw(win)


def draw_patch_window():
    win = Window("",200,200)
    tl = Point(0,0)
    start_x = tl.x
    start_y = tl.y
    for Y in range(start_y , 100,20):
        for X in range(start_x,100,20):
            p1 = Point(X,Y)
            t1=Point(X+10,Y+10)
            p2 = Point(X + 20,Y+20)
            rectangle(win,p1,p2,"white","red")
            text(win,t1,"hi!",5)
    win.get_mouse()
    win.close()


def rectangle2(win,p1,p2,colour):
    rect = Rectangle(p1,p2)
    rect.fill_colour = colour
    rect.draw(win)



def patches():
    win = Window("",200,200)
    for Y in range(0,100,10):
        for X in range(0,100,10):
            tl = Point(X,Y)
            br = Point(X+10,Y+10)
            if (X+Y > 90) or (X+Y== 90):
                rectangle2(win,tl,br,"red")

    win.get_mouse()
    win.close()

def rect3(win,p1,p2,colour):
    rect = Rectangle(p1,p2)
    rect.fill_colour = colour
    rect.draw(win)


def patchesreal3():
    win = Window("",500,500)
    flag = True
    diff = 100
    tl = Point(0,0)
    br = Point(500,500)
    tl2 = Point(100,100)
    br2 = Point(400,400) 
    
    for i in range(0,500,100):
        if flag:
            tl = Point(i,i)
            br = Point(500-(i),500-(i))
            if tl.x// 100 == 2 or 4 or 6:  
                rectangle2(win,tl,br,"red")
            print(tl,br)
            if tl.x >= br.y:
                flag == False
        if flag == False:
            for j in range(100,500,100):
                tl2 = Point(j,j)
                br2 = Point(400- j,400 - j)
                print("if statement reached")
                rectangle2(win,tl,br,"blue")
                print("after")
                if tl2.x >= br2.y:
                    break
    

    win.get_mouse()
    win.close()

def patchesrealreal():
    win = Window()
    tl = Point(0,0)
    br = Point(400,400)
    tl2 = Point(0,0)
    br2 = Point(400,400)
    diff = 20
    for i in range(0,400,20):
        rectangle2(win,tl,br,"red")
        tl =Point(i,i)
        br = Point(br.x -diff,br.y-diff)
        print(tl,br)
        if tl.x >= br.y:
            for j in range(20,400,20):
                tl2 =Point(j,j)
                br2 = Point(400-diff,400-diff)
                rectangle2(win,tl2,br2,"blue")
                print(tl2,br2)
                if tl2.x >= br2.y:
                    break
                pass
    win.get_mouse()
    win.close()

                
def patchesrealrealreal():
    win = Window()
    tl = Point(0,0)
    br = Point(400,400)

    flag = True
    

    for i in range(0,100,5):
        if tl.x >= br.y:
            break
        if (flag):
            tl = Point(i,i)
            br = Point(100-i,100-i)
            rectangle2(win,tl,br,"red")
            print("1",br , tl)
            flag = False
        else:
            tl2 = Point(i,i)
            br2 = Point(100-i,100-i)
            print("2", br2 ,tl2)
            rectangle2(win,tl2,br2,"white")
            flag = True
            print(f" flag is {flag}")
    win.get_mouse()
    win.close()


def eyes_all_around():
    win = Window()
    colours = ["blue","grey","green","brown"]
    for i in range(30):
        click = win.get_mouse()
        colour = colours[i%4]
        draw_eye_help(win,click,30,colour)
    win.get_mouse()
    win.close()



def arch_help(win,center,rad):
    circ = Circle(center,rad)
    circ.fill_colour = "yellow"
    circ.draw(win)
    circ1 = Circle(center,rad//2)
    circ1.fill_colour = "red"
    circ1.draw(win)
    circ2 = Circle(center,rad//4)
    circ2.fill_colour = "blue"
    circ2.draw(win)

def arrows(win,center,rad):
    arrow = Circle(center,rad)
    arrow.fill_colour= "black"
    arrow.draw(win)
def distance_between_points(p1,p2):
    return ((p2.x-p1.x)**2 + (p2.y-p1.y)**2)**0.5

def archery():
    win = Window("",500,500)
    arch_help(win,Point(250,250),100)
    blue = 25
    red = 50
    yellow = 100
    text = Text(Point(50,400),"")
    text2 = Text(Point(50,350),"")
    text3 = Text(Point(400,400),"")
    text3.draw(win)
    text2.draw(win)
    text.draw(win)
    counter = 0

    for i in range(5):
        wind = random.randint(1,5)
        rain = random.randint(1,5)
        
        text.text ="wind"+ str(wind)
        text2.text = "rain"+str(rain)
        click = win.get_mouse()
        click = Point(click.x+(wind*10),click.y+(rain*10))
        dist = distance_between_points(click,Point(250,250))
        if dist <= blue:
            counter += 2
            text3.text = "Points "+str(counter)
        elif dist <= red:
            counter+= 5
            text3.text = "Points "+str(counter)
        elif dist < yellow:
            counter+= 10
            text3.text = "Points "+str(counter)

        arrows(win,click,5)
        



    win.get_mouse()
    win.close()

archery()

