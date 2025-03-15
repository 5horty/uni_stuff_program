from backfinal import SmartHome,SmartDoorBell,SmartLight,SmartPlug
from tkinter import Tk, Frame,Label,Button,StringVar

class SmartHomeApp:
    buttons = {}
    labels ={}

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
        #self.create_labels()
        self.create_buttons()
        self.win.mainloop()

    def update_labels(self):
        for device_id, item in self.labels.items():
            index = next((i for i, d in enumerate(self.smart_home.device_list) if id(d) == device_id),None)
            if index is not None:
                device = self.smart_home.device_list[index]
                text = f"{index+1}: {str(device)}"
                item.config(text = text)

    def turn_on_all(self):
        self.smart_home.switch_all_on()
        self.update_labels()

    def turn_off_all(self):
        self.smart_home.switch_all_off()
        self.update_labels()


    def toggle_btn(self,device_id):
        index = next((i for i, d in enumerate(self.smart_home.device_list) if id(d) == device_id),None)
        if index is not None:
            self.smart_home.device_list[index].toggle_switch()
            self.update_labels()

    def delete_btn(self,device_id):
        index = next((i for i, d in enumerate(self.smart_home.device_list) if id(d) == device_id),None)
        if index is not None:
            self.smart_home.remove_device(index)
            self.remove_labels(device_id)
            self.remove_btns(device_id)
            self.update_labels()

    def remove_btns(self,device_id):
        if device_id in self.buttons:
            print(self.buttons[device_id])
            for btn in self.buttons[device_id]:
                btn.destroy()
        self.buttons.pop(device_id)
    
    def remove_labels(self,device_id):
        if device_id in self.labels:
            self.labels[device_id].destroy()
            self.labels.pop(device_id)

    def create_labels(self):
        for i , items in enumerate(self.smart_home.device_list):
            devices = Label(
                self.main_frame,
                text= f"{i+1}: {str(items)}"
            )
            devices.grid(row = 1,column= 0,columnspan=2,rowspan=row,sticky= "nesw")

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
            command= self.turn_off_all
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
            toggle_btn.grid(row = 1+i,column= 2,sticky="nesw")
            delete_btn = Button(
                self.main_frame,
                text = "delete",
                command= lambda id = device_id :self.delete_btn(id)
                )
            delete_btn.grid(row=1+i,column=4)
            edit_btn = Button(
                self.main_frame,
                text = "edit",
                command= lambda id = device_id :self.delete_btn(id)
                )
            edit_btn.grid(row=1+i,column=3)

            devices = Label(
                self.main_frame,
                text= f"{i+1}: {str(items)}"
            )
            devices.grid(row = i+1,column= 0,columnspan=2,sticky= "nesw")
            buttons_row.append(toggle_btn)
            buttons_row.append(delete_btn)
            print(buttons_row)
            self.buttons[device_id] = [toggle_btn,delete_btn,edit_btn]
            self.labels[device_id] = devices
            print(self.buttons)
            

        











def run():
    t = SmartHomeApp()
    t.run()

run()
