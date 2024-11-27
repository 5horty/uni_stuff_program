from graphix import Circle, Rectangle,Polygon,Text,Window, Point




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
    rect.draw(win)
    tl2 = Point(size-100,p1)
    br2 = Point(size,p1+100)
    rect2 = Rectangle(tl2,br2)
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


def pen_patch(win,colour2,y,x):
    tl = Point(x,y)
    start_x = tl.x
    start_y = tl.y
    for Y in range(start_y , start_y+100,20):
        for X in range(start_x,start_x+100,20):
            p1 = Point(X,Y)
            p2 = Point(X+20,Y+20)
            rectangle(win,p1,p2,colour2,colour2)
                  
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



def main():
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

    win = Window("up2274850",size,size)
    for y in range(0,size,200):
        rectangle2(win,y+100,colour,size)
        for x in range(0,size,100):
            if y == 0 or y == size-100:
                draw_patch_window(win,colour,y,x)
            draw_patch_window(win,colour,y,0)
            draw_patch_window(win,colour,y,size-100)
        #            if (size-100) < (x+ y):
 #               pen_patch(win,colour2,y,x)
  #          if (size-100) > (x+ y) or (size-100) == (x+y) :
   #             pen_patch(win,colour3,y,x)
#        elif (y % 200) == 0:
 #           for x2 in range(100,size-100,100):
  #              pen_pacth(win,colour2,y,x2)
            
        
    

    patches(win,colour2,size,colour3)
    win.get_mouse()
    win.close()

main()
