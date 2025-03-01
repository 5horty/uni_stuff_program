from backfinal import SmartHome,SmartDoorBell,SmartLight,SmartPlug
from tkinter import Tk, Frame,Label,Button,StringVar
class Gui:
    buttons = {}
    button_ids =[]
    def __init__(self):
        self.win = Tk()
        self.win.title("SmartHome")
        self.win.geometry("500x500")
        self.main_frame = Frame(self.win)
        self.main_frame.pack()
        self.strvar = StringVar()

        self.smart_home = SmartHome()
        self.smart_home.add_device(SmartDoorBell())
        self.smart_home.add_device(SmartLight())
        self.smart_home.add_device(SmartPlug(100))

        self.strvar.set(self.smart_home)


    def turn_on_all(self):
        self.smart_home.switch_all_on()
        self.strvar.set(self.smart_home)

    def turn_off_all(self):
        self.smart_home.switch_all_off()
        self.strvar.set(self.smart_home)

    def printAll(self):
        print(self.smart_home)

    def toggle_device(self,device_index):
        self.smart_home.device_list[device_index].toggle_switch()
        self.strvar.set(self.smart_home)

    def remove_button(self,button_id):
        self.buttons[button_id].destroy()
        del self.buttons[button_id] 

    def delete(self,device_index,button_id):
        self.smart_home.remove_device(device_index)
        self.strvar.set(self.smart_home)
        self.remove_button(button_id)
    

    def run(self):
        self.create_widgets()
        self.win.mainloop()


    def create_widgets(self):
        turn_on = Button(
            self.main_frame,
            text="Turn all on",
            command=self.turn_on_all
        )
        turn_on.id = "btn1"
        self.buttons[turn_on.id] = turn_on
        turn_on.grid(row = 0, column = 0,ipadx = 75, columnspan = 2,sticky = 'we')

        turn_off = Button(
            self.main_frame,
            text="Turn all off",
            command=self.turn_off_all
        )
        turn_off.grid(row = 0, column = 3,ipadx = 75,columnspan = 2, sticky = 'we')

        for i in range(len(self.smart_home.device_list)):

            toggle = Button(self.main_frame,
                text="toggle",
                command=lambda idx = i: self.toggle_device(idx) 
                            )
            toggle.id = f"toggle{i}"
            self.buttons[toggle.id] = toggle
            toggle.grid(row = 1+i  , column = 3,rowspan = 1,sticky = "we")

            edit= Button(self.main_frame,
                text="edit",
                command=lambda idx = i: self.toggle_device(idx) #not done last thing need to add hardsest
                            )
            edit.id = f"edit{i}"
            self.buttons[edit.id] = edit
            edit.grid(row = 1+i  , column = 4,rowspan = 1,sticky = "we")

            delete= Button(self.main_frame,
                text="delete",
                command=lambda idx = i: self.delete(idx,f"delete{i}") 
                            )
            delete.id = f"delete{i}"
            print(delete.id)
            self.buttons[delete.id] = delete
            delete.grid(row = 1+i  , column = 5,rowspan = 1,padx = 10,sticky = "we")

        display = Label(
            self.main_frame,
            textvariable = self.strvar
        )
        display.grid(row = 1,column =0,columnspan = 2,rowspan = 3,sticky = 'wens')



    


def test():
    t= Gui()
    t.run()

test()
