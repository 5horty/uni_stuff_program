from graphix import Rectangle,Text,Window,Point
import time

def rectangle(win,tl,br,out_colour,colour):
    rect = Rectangle(tl,br)
    rect.outline_colour = out_colour
    rect.fill_colour = colour
    rect.draw(win)
    return rect

def border(win,p1):
    br = Point(p1.x + 100,p1.y + 100)
    rect = Rectangle(p1,br)
    rect.outline_width = 8
    rect.outline_colour = "black"
    rect.draw(win)
    return rect

def text(win,point,colour,size):
    texts = Text(point,"hi!")
    texts.fill_colour = colour
    texts.size = size
    texts.draw(win)
    return texts

def undraw_stuff(patch_obj):
    if type(patch_obj) == list:
        for item in patch_obj:
            item.undraw()
    else:
        patch_obj.undraw()

def move_patch(patch_obj,x_amount,y_amount):
    if type(patch_obj) == list:
        for item in patch_obj:
            item.move(x_amount,y_amount)
            time.sleep(0.01)
    else:
        patch_obj.move(x_amount,y_amount)
    return patch_obj 
    
def box_click(win,tl_point):
    xclick = (tl_point.x//100)*100
    yclick = (tl_point.y//100)*100
    patch_border = border(win,Point(xclick,yclick))
    return patch_border
   
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
                patch_obj.append(rect_long)
        else:
            for column2 in range(start_y,start_y+100,20):
                tl = Point(row,column2)
                br = Point(row+10,column2+20)
                if ((column2-start_y)//20)%2 ==0:
                    rect_short = rectangle(win,tl,br,"black",colour)
                    patch_obj.append(rect_short)
                else:
                    rect_short_other = rectangle(win,tl,br,"black","white")
                    patch_obj.append(rect_short_other)
    return patch_obj
    
    #undraw_stuff(patch_obj)
    
def check_keys(win,grid,colour,colour2,colour3,size):
    border_grid = {}
    click = win.get_mouse()
    patch_border_x = click.x//100*100
    patch_border_y = click.y//100*100
    border = box_click(win,click)
    border_grid[(patch_border_x,patch_border_y)] = border
    while True:
        key = win.get_key()
        patch_x = click.x//100*100
        patch_y = click.y//100*100
        match key:
            case "x":
                undraw_stuff(grid[(patch_x,patch_y)])
                grid.pop((patch_x,patch_y))
            case "1":
                if (patch_x,patch_y)not in grid:
                    patch = pen_patch(win,colour,patch_x,patch_y)
                    grid[(patch_x,patch_y)] = patch
            case "2":
                if (patch_x,patch_y)not in grid:
                    patch = pen_patch(win,colour2,patch_x,patch_y)
                    grid[(patch_x,patch_y)] = patch
            case "3":
                if (patch_x,patch_y)not in grid:
                    patch = pen_patch(win,colour3,patch_x,patch_y)
                    grid[(patch_x,patch_y)] = patch
            case "4":
                if (patch_x,patch_y)not in grid:
                    patch = draw_final_patch(win,colour,patch_x,patch_y)
                    grid[(patch_x,patch_y)] = patch
            case "5":
                if (patch_x,patch_y)not in grid:
                    patch = draw_final_patch(win,colour2,patch_x,patch_y)
                    grid[(patch_x,patch_y)] = patch
            case "6":
                if (patch_x,patch_y)not in grid:
                    patch = draw_final_patch(win,colour3,patch_x,patch_y)
                    grid[(patch_x,patch_y)] = patch
            case "7":
                if (patch_x,patch_y)not in grid:
                    tl = Point(patch_x,patch_y)
                    br = Point(patch_x+100,patch_y+100)
                    patch = draw_final_patch(win,tl,br,colour,colour)
                    grid[(patch_x,patch_y)] = patch
            case "8":
                if (patch_x,patch_y)not in grid:
                    tl = Point(patch_x,patch_y)
                    br = Point(patch_x+100,patch_y+100)
                    patch = rectangle(win,tl,br,colour2,colour2)
                    grid[(patch_x,patch_y)] = patch
            case "9":
                if (patch_x,patch_y)not in grid:
                    tl = Point(patch_x,patch_y)
                    br = Point(patch_x+100,patch_y+100)
                    patch = rectangle(win,tl,br,colour3,colour3)
                    grid[(patch_x,patch_y)] = patch
            case "Up":
                if (patch_x,patch_y-100)not in grid and patch_y >= 0:
                    patch = move_patch(grid[(patch_x,patch_y)],0,-100)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x,patch_y-100)] = patch
            case "Down":
                if (patch_x,patch_y+100)not in grid and patch_y+100 <= size:
                    patch = move_patch(grid[(patch_x,patch_y)],0,100)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x,patch_y+100)] = patch
            case "Left":
                if (patch_x-100,patch_y)not in grid and patch_x >= 0:
                    patch = move_patch(grid[(patch_x,patch_y)],-100,0)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x-100,patch_y)] = patch
            case "Right":
                if (patch_x+100,patch_y)not in grid and patch_x <= size :
                    patch = move_patch(grid[(patch_x,patch_y)],+100,0)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x+100,patch_y)] = patch
            case "Escape":
                undraw_stuff(border_grid[(patch_border_x,patch_border_y)])
                border_grid.pop((patch_border_x,patch_border_y))
                click = win.get_mouse()
                patch_border_x = click.x//100*100
                patch_border_y = click.y//100*100
                border = box_click(win,click)
                border_grid[(patch_border_x,patch_border_y)] = border





def draw_final_patch(win,colour,x,y):
    patch_obj = []
    start_x = x
    start_y = y
    for column in range(start_y,start_y+100,20):
        for row in range(start_x,start_x+100,20):
            tl = Point(row,column)
            point = Point(row+10,column+10)
            br = Point(row+20,column+20)
            rect = rectangle(win,tl,br,colour,"white")
            patch_obj.append(rect)
            texts = text(win,point,colour,5)
            patch_obj.append(texts)
    return patch_obj

def check_vals():
    val_sizes = ["5","7","9"]
    val_colours = ["red","green","blue","magenta","orange","purple"]

    size = input("Enter a window size (5,7,9): ")
    size = size.strip()
    while size not in val_sizes:
        size = input("Not valid size enter a valid size: ")
        size = size.strip()
    size = int(size)
    size = size * 100

    colour = input("""Enter the first colour 
(red, greem, blue, magenta, orange, purple): """)
    colour = colour.strip()
    while colour.lower() not in val_colours or colour.isdigit():
        colour = input("Not valid colour enter a valid colour: ")
        colour = colour.strip()
        
    colour2 = input("Enter the second colour: ")
    colour2 = colour2.strip()
    while colour2.lower() not in val_colours or colour2.isdigit():
        colour2 = input("Not valid colour enter a valid colour: ")
        colour2 = colour2.strip()
        


    colour3 = input("Enter the third colour: ")
    colour3 = colour3.strip()
    while colour3.lower() not in val_colours or colour.isdigit():
        colour3 = input("Not valid colour enter a valid colour: ")
        colour3 = colour3.strip()

    return size,colour,colour2,colour3
    

def loops(win,size,colour,colour2,colour3):
    grid = {}
    
    
    for column in range(0,size,100):
        if (column//100)%2 == 0 and not column ==0 and not column == size-100:
            patch = draw_final_patch(win,colour,size-100,column)
            grid[(size-100,column)] = patch
            patch = draw_final_patch(win,colour,0,column)
            grid[(0,column)] =patch
        if (column//100)%2 == 1:
            tl = Point(0,column)
            br = Point(100,column+100)
            patch = rectangle(win,tl,br,colour,colour)
            grid[(tl.x,tl.y)] = patch
            tl = Point(size-100,column)
            br = Point(size,column+100)
            patch = rectangle(win,tl,br,colour,colour)
            grid[(tl.x,tl.y)] = patch
        for row in range(0,size,100):
            if column == 0 or column == size-100:
                patch = draw_final_patch(win,colour,row,column)
                grid[(row,column)] = patch
            else:
                if row >= 100 and row <= size-100:
                    tl = Point(row,column)
                    br = Point(row+100,column+100)
                    if (column//100)%2 == 0 and (column+row) <= size-100:
                        patch = pen_patch(win,colour3,row,column)
                        grid[(row,column)] = patch
                    if (column//100)%2 == 0  \
                            and (column+row) > size-100 \
                            and row+100 <= size-100:

                        patch = draw_final_patch(win,colour2,row,column)
                        grid[(row,column)] = patch
                    if (column//100)%2 == 1 \
                            and (column+row) > size-100 \
                            and row+100 <= size-100:

                        patch = rectangle(win,tl,br,colour2,colour2)
                        grid[(row,column)] = patch
                    if (column//100)%2 == 1 and (column+row) <= size-100:
                        patch = rectangle(win,tl,br,colour3,colour3)
                        grid[(row,column)] = patch
    
    check_keys(win,grid,colour,colour2,colour3,size)


def main():
    size,colour,colour2,colour3 = check_vals()
    win = Window("",size,size)
    loops(win,size,colour,colour2,colour3)

    win.close()

main()

