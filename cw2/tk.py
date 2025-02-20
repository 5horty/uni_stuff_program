from tkinter import Tk, Label, Button

class MysteryApp1:
    def __init__(self):
        self.win = Tk()
        self.win.title("Mystery Window 1")
        self.win.geometry("200x200")
        self.create_widgets()
    
    def create_widgets(self):
        label = Label(
            self.win,
            text="Welcome to Mystery Window"
        )
        label.pack(side="left")
        
        button = Button(
            self.win,
            text="ok"
        )
        button.pack(side="right")
        
    def run(self):
        self.win.mainloop()


def main():
    app = MysteryApp1()
    app.run()

main()





from tkinter import Tk, Label, Button

class MysteryApp2:
    def __init__(self):
        self.win = Tk()
        self.win.title("Mystery Window 2")
        self.win.geometry("300x200")
        self.create_widgets()
    
    def create_widgets(self):
        label = Label(
            self.win,
            text="Welcome to Tkinter!"
        )
        label.pack()
        button = Button(
            self.win,
            text="Click Me",
            command=self.on_click
        )
        button.pack()
    
    def on_click(self):
        print("Button clicked!")
    
    def run(self):
        self.win.mainloop()


def main():
    app = MysteryApp2()
    app.run()

main()

