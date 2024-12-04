from graphix import Circle, Rectangle,Polygon,Text,Window, Point


def test(win,p1):
    br = Point(p1.x + 100,p1.x + 100)
    rect = Rectangle(p1,br)
    rect.outline_width = 5
    rect.outline_colour = "black"
    rect.draw(win)

def rectangle(win,point1,point2,out_colur,colour):
    rect = Rectangle(point1,point2)
    rect.outline_colour = out_colur
    rect.fill_colour = colour
    rect.draw(win)

def text(win,point1,texts,size,colour):
    textz = Text(point1,texts)
    textz.fill_colour = colour
    textz.size = size
    textz.draw(win)

def rectangle2(win,p1,colour,size):
    tl = Point(0,p1)
    br = Point(100,p1+100)
    rect = Rectangle(tl,br)
    rect.fill_colour = colour
    rect.outline_colour = "black"
    rect.draw(win)
    tl2 = Point(size-100,p1)
    br2 = Point(size,p1+100)
    rect2 = Rectangle(tl2,br2)
    rect2.outline_colour = "black"
    rect2.fill_colour = colour
    rect2.draw(win)

def patches(win,colour2,size,colour3):
    for Y in range(100,size-100,100):
        for X in range(100,size-100,100):
            tl = Point(X,Y)
            br = Point(X+100,Y+100)
            if (X+Y > size-100):
                rectangle(win,tl,br,colour2,colour2)
            else:
                rectangle(win,tl,br,colour3,colour3)







def pen_patch(win,colour,y,x):
   p = Point(x,y)
   start_x = p.x
   start_y = p.y
   for X in range(start_x,start_x+100,10):
       if (X//10)%2 == 1:
           for Y in range(start_y,start_y+100,25):
               tl = Point(X,Y)
               br = Point(X+10,Y+25)
               rectangle(win,tl,br,"black",colour)
       else:
            for Y2 in range(start_y,start_y+100,20):
                tl = Point(X,Y2)
                br = Point(X+10,Y2+20)
                if (Y2//20)%2 == 0:
                    rectangle(win,tl,br,"black",colour)
                else:
                    rectangle(win,tl,br,"black","white")
def draw_patch_window(win,colour,y,x):
    tl = Point(x,y)
    start_x = tl.x
    start_y = tl.y
    for Y in range(start_y , start_y+100,20):
        for X in range(start_x,start_x+100,20):
            p1 = Point(X,Y)
            t1=Point(X+10,Y+10)
            p2 = Point(X + 20,Y+20)
            rectangle(win,p1,p2,colour,"white")
            text(win,t1,"hi!",5,colour)

def check_vals():
    val_sizes = [5,7,9]
    val_colours = ["red","green","blue","magenta","orange","purple"]

    size = int(input("enter a window sixe (5,7,9): "))
    while size not in val_sizes:
        size = int(input("not valid size enter a valid size: "))
    size = size * 100

    colour = input("enter a colour: ")
    while colour.lower() not in val_colours:
        colour = input("not valid colour enter a valid colour: ")

    colour2 = input("enter a colour: ")
    while colour2.lower() not in val_colours:
        colour2= input("not valid colour enter a valid colour: ")


    colour3 = input("enter a colour: ")
    while colour3.lower() not in val_colours:
        colour3=input("not valid colour enter a valid colour: ")
    return size,colour,colour2,colour3


def check_keys(win,size):
    co_ords = [[tl_x for tl_x in range(0,size,100)],
               [br_x for br_x in range(100,size+100,100)],
               [tl_y for tl_y in range(0,size,100)],
               [br_y for br_y in range(100,size+100,100)]]
    for y in range(len(co_ords[0])):
        for x in range(len(co_ords[0])):
            print(f"tl: {co_ords[0][x]},{co_ords[2][y]} - br: {co_ords[1][x]},{co_ords[3][y]}")

    click = win.get_mouse()
    xclick = (click.x//100)*100
    yclick = (click.y//100)*100
    test(win,Point(xclick,yclick))
    #print(xclick,yclick)
    
        




def main():
    size,colour,colour2,colour3 = check_vals()

    win = Window("up2274850",size,size)
    patches(win,colour2,size,colour3)
    for y in range(0,size,200):
        rectangle2(win,y+100,colour,size)
        for x in range(0,size,100):
            if y == 0 or y == size-100:
                draw_patch_window(win,colour,y,x)
            elif (y//100)%2 == 0:
                pen_patch(win,colour3,y,x)
            if (y//100)%2 == 0 and (x+y) > size-100 and not y== size-100:
                draw_patch_window(win,colour2,y,x)
            draw_patch_window(win,colour,y,0)
            draw_patch_window(win,colour,y,size-100)

    check_keys(win,size)
    win.get_mouse()
    win.close()

main()

