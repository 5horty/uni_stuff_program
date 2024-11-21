from graphix import Window, Circle, Rectangle,Point,Text,Entry


# Constants
SCREEN = 500
TILE = 100
RADIUS = 50
SMALL_TILE = 20
SMALL_RADIUS = 10

# Function to draw a rectangle with specified parameters
def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.draw(win)

# Function to draw a circle with specified parameters
def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.draw(win)


def patch_2(win,tl_point,colour):

    start_x = tl_point.x
    start_y = tl_point.y
    for y in range(start_y, 100+start_y, 20):
        for x in range(start_x, 100+start_x, 20):
            if (x == y) or (x + y == 100-20):
                center = Point(x + 10, y + 10)
                draw_circle(win,center,10,"red")
            else:
                p1 = Point(x, y)
                p2 = Point(x + 20, y + 20)
                draw_rectangle(win, p1, p2, "blue") 





def patch_1(win,tl_point,colour):
    start_x = tl_point.x
    start_y = tl_point.y
    for Y in range(start_y, 100+start_y, 20):
        for X in range(start_x, 100+start_x, 20):
            # Draw rectangle
            p1 = Point(X, Y)
            p2 = Point(X + 20, Y + 20)
            draw_rectangle(win, p1, p2, "blue")
            # Draw circle
            center = Point(X + 10, Y + 10)
            draw_circle(win, center, 10, "red")
    

def program():
    
    win = Window("Tiled Rectangles with Circles", 800, 800)
    tl = win.get_mouse()
    patch_2(win,tl,"red")
    tl2 = win.get_mouse()
    patch_1(win,tl2,"red")  
    win.get_mouse()
    win.close()

program()

