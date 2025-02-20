from tkinter import Tk, Frame,Label


class LoginApp:

    def __init__(self):
        self.win = Tk()
        self.win.title("Employee Login")
        self.win.geometry("300x100")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)
        
    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_message = Label(
            self.main_frame,
            text="Enter username and password."
        )
        label_message.grid(column=0, row=0)

def main():
    app = LoginApp()
    app.run()



class TestLogin:
    def __init__(self):
        self.win = Tk()
        self.win.title("testing")
        self.win.geometry("200x200")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=1,row=1)
    def run(self):
        #self.create_widgets()
        self.win.mainloop()


def main():
    app = TestLogin()
    app.run()

main()

