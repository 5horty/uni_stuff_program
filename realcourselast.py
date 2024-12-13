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
    rect.outline_width = 5
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
    if isinstance(patch_obj,list):
        for i in patch_obj:
            i.undraw()
    else:
        patch_obj.undraw()
        
    
def box_click(win,size,tl_point):
    patch_obj = []
    xclick = (tl_point.x//100)*100
    yclick = (tl_point.y//100)*100
    patch_border = border(win,Point(xclick,yclick))
    patch_obj.append(patch_border)
    return patch_obj
   
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
                if (column2//20)%2 ==0:
                    rect_short = rectangle(win,tl,br,"black",colour)
                    patch_obj.append(rect_short)
                else:
                    rect_short_other = rectangle(win,tl,br,"black","white")
                    patch_obj.append(rect_short_other)
    return patch_obj
    
    #undraw_stuff(patch_obj)
    


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


def check_keys(win,size,grid,colour,colour2,colour3):
    flag = True
    click = win.get_mouse()
    patchx_b , patchy_b = click.x //100*100,click.y//100*100
    patch_border = box_click(win,size,click)
    grid[(patchx_b,patchy_b)] = patch_border
    while flag:
        key = win.get_key()
        match key:
            case "x":
                patchx , patchy = click.x //100*100,click.y//100*100
                undraw_stuff(grid[(patchx,patchy)])
                grid.pop(patchx,patchy)
                draw_key = win.get_key()
                if draw_key == "Escape":
                    undraw_stuff(grid[(patchx_b,patchy_b)])
                    grid.pop(patchx_b,patchy_b)
                while draw_key != "Escape":
                    if draw_key == "x":
                        match draw_key:
                            case "1":
                                patch_redraw_x , patch_redraw_y = click.x //100*100,click.y//100*100
                                patch = pen_patch(win,colour,patch_redraw_x,patch_redraw_y)
                                grid[(patch_redraw_x,patch_redraw_y)] = patch
                            case "2":
                                patch_redraw_x , patch_redraw_y = click.x //100*100,click.y//100*100
                                patch = pen_patch(win,colour2,patch_redraw_x,patch_redraw_y)
                                grid[(patch_redraw_x,patch_redraw_y)] = patch
                            case "3":
                                patch_redraw_x , patch_redraw_y = click.x //100*100,click.y//100*100
                                patch = pen_patch(win,colour3,patch_redraw_x,patch_redraw_y)
                                grid[(patch_redraw_x,patch_redraw_y)] = patch
                            case "x":
                                patchx , patchy = click.x //100*100,click.y//100*100
                                undraw_stuff(grid[(patchx,patchy)])
                                grid.pop(patchx,patchy)
                    draw_key = win.get_key()

            case "Escape":
                undraw_stuff(grid[(patchx_b,patchy_b)])
                print(grid[(patchx_b,patchy_b)])
                grid.pop(patchx_b,patchy_b)
                print(grid[(patchx_b,patchy_b)])
        
        click = win.get_mouse()
        patchx_b , patchy_b = click.x //100*100,click.y//100*100
        patch_border = box_click(win,size,click)
        grid[(patchx_b,patchy_b)] = patch_border

        
        

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
                    if (column//100)%2 == 0 and (column+row) <= size-100:
                        patch = pen_patch(win,colour3,row,column)
                        grid[(row,column)] = patch
                    if (column//100)%2 == 0 and (column+row) > size-100 and row+100 <= size-100:
                        patch = draw_final_patch(win,colour2,row,column)
                        grid[(row,column)] = patch
                    if (column//100)%2 == 1 and (column+row) > size-100 and row+100 <= size-100:
                        patch = rectangle(win,Point(row,column),Point(row+100,column+100),colour2,colour2)
                        grid[(row,column)] = patch
                    if (column//100)%2 == 1 and (column+row) <= size-100:
                        patch = rectangle(win,Point(row,column),Point(row+100,column+100),colour3,colour3)
                        grid[(row,column)] = patch
    
    check_keys(win,size,grid,colour,colour2,colour3)


def main():
    size,colour,colour2,colour3 = check_vals()
    win = Window("",size,size)
    loops(win,size,colour,colour2,colour3)

    win.close()

main()
