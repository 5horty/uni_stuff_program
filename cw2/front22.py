from backfinal import SmartHome,SmartDoorBell,SmartLight,SmartPlug
from tkinter import Tk, Frame,Label,Button,StringVar,Toplevel,Entry,OptionMenu

class SmartHomeApp:
    buttons = {}
    labels ={}
    add_btn_list =[]

    def __init__(self):
        self.win = Tk()
        self.win.title("SmartHome")
        self.win.geometry("1200x620")
        self.win.minsize(1200,620)
        self.win.maxsize(1200,620)
        self.main_frame = Frame(self.win)
        self.main_frame.pack()

        self.smart_home = SmartHome()
        self.smart_home.add_device(SmartDoorBell())
        self.smart_home.add_device(SmartLight())
        self.smart_home.add_device(SmartPlug(45))



    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def update_labels(self):
        for device_id, item in self.labels.items():
            index = next((i for i, d in enumerate(self.smart_home.device_list)
                if id(d) == device_id),None)
            if index is not None:
                device = self.smart_home.device_list[index]
                text = f"{index+1}: {str(device)}"
                item.config(text = text)
        self.main_frame.update()

    def turn_on_all(self):
        self.smart_home.switch_all_on()
        self.update_labels()

    def turn_off_all(self):
        self.smart_home.switch_all_off()
        self.update_labels()


    def toggle_btn(self,device_id):
        index = next((i for i, d in enumerate(self.smart_home.device_list)
            if id(d) == device_id),None)
        if index is not None:
            self.smart_home.device_list[index].toggle_switch()
            self.update_labels()

    def delete_btn(self,device_id):
        index = next((i for i, d in enumerate(self.smart_home.device_list)
            if id(d) == device_id),None)
        if index is not None:
            self.smart_home.remove_device(index)
            self.remove_labels(device_id)
            self.remove_btns(device_id)
            self.update_labels()

    def remove_btns(self,device_id):
        if device_id in self.buttons:
            for btn in self.buttons[device_id]:
                btn.destroy()
        self.buttons.pop(device_id)
    
    def remove_labels(self,device_id):
        if device_id in self.labels:
            self.labels[device_id].destroy()
            self.labels.pop(device_id)

    def edit_btn(self,device_id):
        device = next((d for d in self.smart_home.device_list 
            if id(d)== device_id), None)
        if device:
            edit_window = Toplevel(self.win)
            edit_window.title("Edit Device")
            edit_window.minsize(520,150)
        
        # Check which attribute of the device
            if isinstance(device, SmartPlug):
                current_value = device.option  #current consumption rate
                label = Label(edit_window, 
                              text="consumption rate:"
                              )
                entry = Entry(edit_window)
                entry.insert(0, str(current_value))  #puts number in front

            elif isinstance(device, SmartLight):
                current_value = device.option  #the current brightness
                label = Label(edit_window, text="Set Brightness:")
                entry = Entry(edit_window)
                entry.insert(0, str(current_value))  

            elif isinstance(device, SmartDoorBell):
                current_value = device.sleep_mode  #current sleep mode status
                label = Label(edit_window, text="Set Sleep Mode (True/False):")
                entry = Entry(edit_window)
                entry.insert(0, str(current_value))  

        # Layout
            label.grid(row=0, column=0)
            entry.grid(row=0, column=1)

            def save_changes():
                try:
                    new_value = entry.get().strip()
                    if isinstance(device, SmartPlug):
                        new_value = int(new_value)
                        device.option = new_value  # Update the consumption rate
                    elif isinstance(device, SmartLight):
                        new_value = int(new_value)
                        device.option = new_value  # Update the brightness
                    elif isinstance(device, SmartDoorBell):
                        if new_value.capitalize() == "True":
                            device.sleep_mode = bool(new_value)
                        elif new_value.capitalize() == "False":
                            device.sleep_mode = False
                        else:
                            device.sleep_mode = 69420

                # Update the device label after editing
                    self.update_labels()
                    self.create_widgets()

                # Close the edit window
                    
                    edit_window.destroy()

                except (ValueError, TypeError) as e:
                    self.error_window(e)

            save_btn = Button(edit_window, text="Save", command=save_changes)
            save_btn.grid(row=1, column=0, columnspan=2)


    def add_btn(self):
        add_window = Toplevel(self.win)
        add_window.title("add device")
        add_window.minsize(500,150)

        label = Label(add_window,
                      text= "choose device"
                      )
        label.grid(row=0,column=0)
        device_var = StringVar(add_window)
        device_var.set("SmartDoorBell")  #default selection
        options = ["SmartDoorBell", "SmartLight", "SmartPlug"]
        dropdown = OptionMenu(add_window, device_var, *options)
        dropdown.grid(row=0, column=1)

        entry = Entry(add_window)
        entry.grid(row = 1, column= 1)
        
        optional_lable = Label(
            add_window,
            text="Optional amount"
            )
        optional_lable.grid(row=1,column=0)

        def add_device():
            device_name = device_var.get()
            value = entry.get().strip()  
            new_device = None

            if device_name == "SmartDoorBell":
                new_device = SmartDoorBell()  
                if value:
                    try:
                        if value.strip().lower() == "false" :
                            new_device.sleep_mode = False
                        elif value.strip().lower() == "true":
                            new_device.sleep_mode = True
                    except (TypeError,ValueError) as e:
                        self.error_window(e)
                        return


            elif device_name == "SmartLight":
                new_device = SmartLight()  
                if value:
                    try:
                        new_device.option = int(value)
                    except (ValueError,TypeError) as e:
                        self.error_window(e)
                        return

            elif device_name == "SmartPlug":
                try:
                    if value:
                        new_device = SmartPlug(int(value)) 
                    else:
                        new_device = SmartPlug(45)  
                except ValueError as e:
                    self.error_window(e)
                    return  

            if new_device:
                try:
                    self.smart_home.add_device(new_device)
                except IndexError as e:
                    self.error_window(e)
                    return


                self.create_widgets()  # update UI

            add_window.destroy()  

        butn = Button(add_window, text="Add", command=add_device)
        butn.grid(row=2, column=0, columnspan=2, sticky="nesw")

    def error_window(self,msg):
        error_win = Toplevel(self.main_frame)
        error_win.title("Error")
        label = Label(
            error_win,
            text = msg
        )
        label.grid()
        btn = Button(
            error_win,
            text="ok",
                command=lambda: error_win.destroy()
            )
        btn.grid()


    def create_widgets(self):
        for btn in self.add_btn_list:
            btn.destroy()

        for button_list in self.buttons.values():
            for button in button_list:
                button.destroy()
        for label in self.labels.values():
            label.destroy()

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
                command= lambda id = device_id :self.edit_btn(id)
                )
            edit_btn.grid(row=1+i,column=3)

            devices = Label(
                self.main_frame,
                text= f"{i+1}: {str(items)}"
            )
            devices.grid(row = i+1,column= 0,columnspan=2,sticky= "nesw")
            self.buttons[device_id] = [toggle_btn,delete_btn,edit_btn]
            self.labels[device_id] = devices
        add_btn = Button(
            self.main_frame,
                text = "add",
                command= self.add_btn
                )
        add_btn.grid()
        self.add_btn_list.append(add_btn)

            

        


        
def test_smart_home_system():
    t = SmartHomeApp()
    print(t.smart_home.device_list)
    t.run()

test_smart_home_system()







def run():
    t = SmartHomeApp()
    t.run()

