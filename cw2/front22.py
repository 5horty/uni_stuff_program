from backfinal import SmartHome,SmartDoorBell,SmartLight,SmartPlug
from tkinter import Tk, Frame,Label,Button,StringVar

class SmartHomeApp:
    buttons = {}

    def __init__(self):
        self.win = Tk()
        self.win.title("SmartHome")
        self.win.geometry("2000x500")
        self.win.minsize(1200,400)
        self.main_frame = Frame(self.win)
        self.main_frame.pack()
        self.strvar = StringVar()

        self.smart_home = SmartHome()
        self.smart_home.add_device(SmartDoorBell())
        self.smart_home.add_device(SmartLight())
        self.smart_home.add_device(SmartPlug(100))

        self.strvar.set(str(self.smart_home))


    def run(self):
        self.create_labels()
        self.create_buttons()
        self.win.mainloop()

    def turn_on_all(self):
        self.smart_home.switch_all_on()
        self.strvar.set(str(self.smart_home))

    def toggle_btn(self,device_id):
        index = next((i for i, d in enumerate(self.smart_home.device_list) if id(d) == device_id),None)
        if index is not None:
            self.smart_home.device_list[index].toggle_switch()
            self.strvar.set(str(self.smart_home))

    def delete_btn(self,device_id):
        index = next((i for i, d in enumerate(self.smart_home.device_list) if id(d) == device_id),None)
        if index is not None:
            self.smart_home.remove_device(index)
            self.strvar.set(str(self.smart_home))
            self.remove_btns(device_id)

    def remove_btns(self,device_id):
        if device_id in self.buttons:
            print(self.buttons[device_id])
            for btn in self.buttons[device_id]:
                btn.destroy()
        self.buttons.pop(device_id)

    def create_labels(self):
        smarthome = Label(
            self.main_frame,
            textvariable= self.strvar 
        )
        smarthome.grid(row = 1,column= 0,columnspan=2,sticky= "nesw")

    def create_buttons(self):
        turn_on_btn = Button(
            self.main_frame,
            text = "turn on all",
            command= self.turn_on_all
        )
        turn_on_btn.grid(row = 0,column=0,columnspan=2,sticky="nesw")
        turn_off_btn = Button(
            self.main_frame,
            text = "turn off all",
            command= self.turn_on_all
        )
        turn_off_btn.grid(row = 0,column=2,columnspan=2,sticky="nesw")

        for i , items in enumerate(self.smart_home.device_list):
            device_id = id(items)
            buttons_row = []
            print(buttons_row)
            toggle_btn = Button(
                self.main_frame,
                text = "toggle",
                command= lambda id = device_id: self.toggle_btn(id)
                )
            toggle_btn.grid(row = 2+i,column= 2,sticky="nesw")
            delete_btn = Button(
                self.main_frame,
                text = "delete",
                command= lambda id = device_id :self.delete_btn(id)
                )
            delete_btn.grid()
            buttons_row.append(toggle_btn)
            buttons_row.append(delete_btn)
            print(buttons_row)
            self.buttons[device_id] = [toggle_btn,delete_btn]
            print(self.buttons)
            

        











def run():
    t = SmartHomeApp()
    t.run()

run()
