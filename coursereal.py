from graphix import Rectangle,Text,Window,Point

def rectangle(win,tl,br,out_colour,colour):
    rect = Rectangle(tl,br)
    rect.outline_colour = out_colour
    rect.fill_colour = colour
    rect.draw(win)
    return rect



def text(win,point,colour,size):
    texts = Text(point,"hi!")
    texts.fill_colour = colour
    texts.size = size
    texts.draw(win)



def pen_patch(win,colour,x,y):
    patch_obj = []
    start_x = x
    start_y = y
    for row in range(start_x,start_x+100,10):
        if (row//10)%2 == 1:
            for column in range(start_y,start_y+100,25):
                tl = Point(row,column)
                br = Point(row+10,column+25)
                rect_long = rectangle(win,tl,br,"black",colour)
                patch_obj.append((tl,br))
        else:
            for column2 in range(start_y,start_y+100,20):
                tl = Point(row,column2)
                br = Point(row+10,column2+20)
                if (column2//20)%2 ==0:
                    rect_short = rectangle(win,tl,br,"black",colour)
                    patch_obj.append((tl,br))
                else:
                    rect_short_other = rectangle(win,tl,br,"black","white")
                    patch_obj.append((tl,br))
    print(patch_obj)

def draw_final_patch(win,colour,x,y):
    start_x = x
    start_y = y
    for column in range(start_y,start_y+100,20):
        for row in range(start_x,start_x+100,20):
            tl = Point(row,column)
            point = Point(row+10,column+10)
            br = Point(row+20,column+20)
            rectangle(win,tl,br,colour,"white")
            text(win,point,colour,5)



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
    

def loops(win,size,colour,colour2,colour3):
    
    for column in range(0,size,100):
        tl = Point(0,column)
        br = Point(100,column+100)
        rectangle(win,tl,br,colour,colour)
        tl = Point(size-100,column)
        br = Point(size,column+100)
        rectangle(win,tl,br,colour,colour)
        for row in range(0,size,100):
            if column == 0 or column == size-100:
                draw_final_patch(win,colour,row,column)
            elif (column//100)%2 == 0:
                pen_patch(win,colour3,row,column)
            if (column//100)%2 == 0 and (column+row) > size-100 and not column == size-100:
                draw_final_patch(win,colour2,row,column)
            elif (column//100)%2 == 1 and (column+row) > size-100:
                    rectangle(win,Point(row,column),Point(row+100,column+100),colour2,colour2)
            elif (column//100)%2 == 1 and (column+row) <= size-100:
                    rectangle(win,Point(row,column),Point(row+100,column+100),colour3,colour3)
            #draw_final_patch(win,colour,0,column)
            #draw_final_patch(win,colour,size-100,column)


def main():
    size,colour,colour2,colour3 = check_vals()
    win = Window("",size,size)
    loops(win,size,colour,colour2,colour3)

    win.get_mouse()
    win.close()

main()




