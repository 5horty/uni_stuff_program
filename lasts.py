from graphix import Rectangle,Text,Window,Point
import time
#rectangle helper function 
def rectangle(win,tl,br,out_colour,colour):
    rect = Rectangle(tl,br)
    rect.outline_colour = out_colour
    rect.fill_colour = colour
    rect.draw(win)
    return rect
#border frame that goes on top
def border(win,p1):
    br = Point(p1.x + 100,p1.y + 100)
    rect = Rectangle(p1,br)
    rect.outline_width = 8
    rect.outline_colour = "black"
    rect.draw(win)
    return rect
#text inside the final patch boxs
def text(win,point,colour,size):
    texts = Text(point,"hi!")
    texts.fill_colour = colour
    texts.size = size
    texts.draw(win)
    return texts
#function that undraws objs for challenge
def undraw_patches(patch_obj):
    if type(patch_obj) == list:
        for item in patch_obj:
            item.undraw()
    else:
        patch_obj.undraw()
#function that moves patchs by specified amount and animation
def move_patch(patch_obj,x_amount,y_amount):
    if type(patch_obj) == list:
        for item in patch_obj:
            item.move(x_amount,y_amount)
            time.sleep(0.01)
    else:
        patch_obj.move(x_amount//2,y_amount//2)
        time.sleep(0.5)
        patch_obj.move(x_amount//2,y_amount//2)

    return patch_obj 
#draws the border around where the patch the user clicks on  
def box_click(win,tl_point):
    xclick = (tl_point.x//100)*100
    yclick = (tl_point.y//100)*100
    patch_border = border(win,Point(xclick,yclick))
    return patch_border
#pen_patch    
def pen_patch(win,colour,x,y):
    patch_obj = []
    start_x = x
    start_y = y
    for row in range(start_x,start_x+100,10):
        if (row//10)%2 == 1:                #if row is even every second one
            for column in range(start_y,start_y+100,25):
                tl = Point(row,column)
                br = Point(row+10,column+25)
                rect_long = rectangle(win,tl,br,"black",colour)
                patch_obj.append(rect_long)
        else:                               #if row is odd
            for column_odd in range(start_y,start_y+100,20):
                tl = Point(row,column_odd) #makes it draw right way every row
                br = Point(row+10,column_odd+20)
                if ((column_odd-start_y)//20)%2 ==0: 
                    rect_short = rectangle(win,tl,br,"black",colour)
                    patch_obj.append(rect_short)
                else:
                    rect_short_other = rectangle(win,tl,br,"black","white")
                    patch_obj.append(rect_short_other)
    return patch_obj
#helper function that draws a patch and updates the grid
def add_patch(win, grid, patch_x, patch_y, colour, draw_func):
    if (patch_x, patch_y) not in grid:
        patch = draw_func(win, colour, patch_x, patch_y)
        grid[(patch_x, patch_y)] = patch

#helper function that draws a rectangle and updates the grid
def add_block(win, grid,patch_x, patch_y, colour, draw_func):
    if (patch_x, patch_y) not in grid:
        tl = Point(patch_x,patch_y)
        br = Point(patch_x+100,patch_y+100)
        patch = draw_func(win,tl,br,colour,colour)
        grid[(patch_x, patch_y)] = patch

    
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
                if (patch_x,patch_y)not in grid:
                    pass
                else:
                    undraw_patches(grid[(patch_x,patch_y)])
                    grid.pop((patch_x,patch_y))
            case "1": #if a key is pressed draws corrisponding patch
                add_patch(win, grid, patch_x, patch_y, colour, pen_patch)
            case "2":
                add_patch(win, grid, patch_x, patch_y, colour2, pen_patch)
            case "3":
                add_patch(win, grid, patch_x, patch_y, colour3, pen_patch)
            case "4":
                add_patch(win, grid, patch_x, patch_y, colour, final_patch)
            case "5":
                add_patch(win, grid, patch_x, patch_y, colour2, final_patch)
            case "6":
                add_patch(win, grid, patch_x, patch_y, colour3, final_patch)
            case "7":
                add_block(win,grid,patch_x,patch_y,colour,rectangle)
            case "8":
                add_block(win,grid,patch_x,patch_y,colour2,rectangle)
            case "9":
                add_block(win,grid,patch_x,patch_y,colour3,rectangle)
            case "Up":#updates patch coordintes and moves patch accordingly
                if (patch_x,patch_y-100)not in grid \
                        and patch_y-100 >= 0 \
                        and (patch_x,patch_y) in grid:
                    patch = move_patch(grid[(patch_x,patch_y)],0,-100)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x,patch_y-100)] = patch
            case "Down":
                if (patch_x,patch_y+100)not in grid \
                        and patch_y+100 < size \
                        and (patch_x,patch_y) in grid:
                    patch = move_patch(grid[(patch_x,patch_y)],0,100)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x,patch_y+100)] = patch
            case "Left":
                if (patch_x-100,patch_y)not in grid \
                        and patch_x-100 >= 0 \
                        and (patch_x,patch_y) in grid:
                    patch = move_patch(grid[(patch_x,patch_y)],-100,0)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x-100,patch_y)] = patch
            case "Right":
                if (patch_x+100,patch_y)not in grid \
                        and patch_x+100 < size \
                        and (patch_x,patch_y) in grid:
                    patch = move_patch(grid[(patch_x,patch_y)],100,0)
                    grid.pop((patch_x,patch_y))
                    grid[(patch_x+100,patch_y)] = patch
            case "Escape":
                undraw_patches(border_grid[(patch_border_x,patch_border_y)])
                border_grid.pop((patch_border_x,patch_border_y))
                click = win.get_mouse()
                patch_border_x = click.x//100*100
                patch_border_y = click.y//100*100
                border = box_click(win,click)
                border_grid[(patch_border_x,patch_border_y)] = border




#draws the final patch
def final_patch(win,colour,x,y):
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
#checks for the user input and does validation checks
def check_vals():
    val_sizes = ["5", "7", "9"]
    val_colours = ["red", "green", "blue", "magenta", "orange", "purple"]

    size = input("Enter a window size (5, 7, 9): ").strip()
    while size not in val_sizes:
        size = input("Not valid size! Enter a valid size (5, 7, 9): ").strip()
    size = int(size) * 100

    selected_colours = set()  # to track chosen colours

    def get_unique_colour(prompt):#gets each colour 
        while True:
            colour = input(prompt).strip().lower()
            if colour in val_colours and colour not in selected_colours:
                selected_colours.add(colour)
                return colour
            elif colour in selected_colours:
                print(f"""You've already chosen '{colour}'.
Please pick a different colour. """)
            else:
                print("Not a valid colour! Enter a valid colour.")

    colour = get_unique_colour("Enter the first colour: ")
    colour2 = get_unique_colour("Enter the second colour: ")
    colour3 = get_unique_colour("Enter the third colour: ")

    return size, colour, colour2, colour3
    

def loops(win,size,colour,colour2,colour3):
    grid = {}
     
    for column in range(0,size,100):
        if (column//100)%2 == 0 and not column ==0 and not column == size-100:
            #draws final patch in left and right most columns in mid patchwork
            add_patch(win, grid, size-100, column, colour, final_patch)
            add_patch(win, grid, 0, column, colour, final_patch)
        if (column//100)%2 == 1:
            #draws rectangle in left and right most columns in mid patchwork
            tl = Point(0,column)
            br = Point(100,column+100)
            patch = rectangle(win,tl,br,colour,colour)
            grid[(tl.x,tl.y)] = patch
            tl = Point(size-100,column)
            br = Point(size,column+100)
            patch = rectangle(win,tl,br,colour,colour)
            grid[(tl.x,tl.y)] = patch
        for row in range(0,size,100):
            #draws the main inside square with 'stairs'
            if column == 0 or column == size-100:
                add_patch(win, grid, row, column, colour, final_patch)
            else:
                if row >= 100 and row <= size-100:
                    tl = Point(row,column)
                    br = Point(row+100,column+100)
                    if (column//100)%2 == 0 and (column+row) <= size-100:
                        add_patch(win, grid, row, column, colour3, pen_patch)
                    if (column//100)%2 == 0  \
                            and (column+row) > size-100 \
                            and row+100 <= size-100:
                        add_patch(win, grid, row, column, colour2, final_patch)

                    if (column//100)%2 == 1 \
                            and (column+row) > size-100 \
                            and row+100 <= size-100:

                        patch = rectangle(win,tl,br,colour2,colour2)
                        grid[(row,column)] = patch
                    if (column//100)%2 == 1 and (column+row) <= size-100:
                        patch = rectangle(win,tl,br,colour3,colour3)
                        grid[(row,column)] = patch
    
    check_keys(win,grid,colour,colour2,colour3,size)
    
    win.close()
#main function
def main():
    size,colour,colour2,colour3 = check_vals()
    win = Window("",size,size)
    loops(win,size,colour,colour2,colour3)


main()

