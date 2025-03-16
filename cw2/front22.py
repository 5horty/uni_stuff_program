from typing import Optional
from backfinal import SmartHome,SmartDoorBell,SmartLight,SmartPlug
from tkinter import Tk, Frame,Label,Button,StringVar,Toplevel,Entry,OptionMenu

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
            for btn in self.buttons[device_id]:
                btn.destroy()
        self.buttons.pop(device_id)
    
    def remove_labels(self,device_id):
        if device_id in self.labels:
            self.labels[device_id].destroy()
            self.labels.pop(device_id)

    def edit_btn(self,device_id):
        device = next((d for d in self.smart_home.device_list if id(d) == device_id), None)
        if device:
            edit_window = Toplevel(self.win)
            edit_window.title("Edit Device")
        
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

        # Save button to update the attribute
            def save_changes():
                try:
                    new_value = entry.get()
                    if isinstance(device, SmartPlug):
                        new_value = int(new_value)
                        device.option = new_value  # Update the consumption rate
                    elif isinstance(device, SmartLight):
                        new_value = int(new_value)
                        device.option = new_value  # Update the brightness
                    elif isinstance(device, SmartDoorBell):
                        new_value = new_value.lower() == 'true'  # Convert to boolean
                        device.sleep_mode = new_value  # Update sleep mode

                # Update the device label after editing
                    self.update_labels()
                    self.create_buttons()

                # Close the edit window
                    
                    edit_window.destroy()

                except (ValueError, TypeError) as e:
                    error_window= Toplevel(self.win)
                    error_window.title("Error")
                    label = Label(error_window,text=f"error: {e}")
                    label.grid()
                    button = Button(error_window,
                                    text= "ok",
                                    command=error_window.destroy
                                    )
                    button.grid()

            save_btn = Button(edit_window, text="Save", command=save_changes)
            save_btn.grid(row=1, column=0, columnspan=2)


    def add_btn(self):
        add_window = Toplevel(self.win)
        add_window.title("add device")

        label = Label(add_window,
                      text= "choose device"
                      )
        label.grid(row=0,column=0)
        device_var = StringVar(add_window)
        device_var.set("SmartDoorBell")  # Default selection
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

        def add_device(device_name, value):
            new_device = None
            value = value.get().strip()  # Get the value from the Entry widget
    
    # Try to convert the value to an integer, handle invalid input
            try:
                value = int(value) if value else None
            except ValueError:
                error_win = Toplevel(add_window)
                Label(error_win, text="Invalid number!").pack()
                Button(error_win, text="OK", command=error_win.destroy).pack()
                return  # Stop execution if the input is invalid

            match device_name:
                case "SmartDoorBell":
                    new_device = SmartDoorBell()  # Initialize the SmartDoorBell
                    if value is not None:
                        pass  # You can set some attribute of SmartDoorBell here if needed
                case "SmartLight":
                    new_device = SmartLight()  # Initialize the SmartLight
                    if value is not None:
                        new_device.option = value  # Set the option (e.g., brightness)
                case "SmartPlug":
                    new_device = SmartPlug(value if value is not None else 100)  # Initialize with value or default to 100
                    if value is not None:
                        new_device.option = value  # Set the option (e.g., power consumption)

    # Add the device to the smart home
            print(self.smart_home.device_list)
            print()
            self.smart_home.add_device(new_device)
            print(self.smart_home.device_list)
    
    # Update the labels on the screen
            self.update_labels()
    
    # Close the add window
            add_window.destroy()

# Button with lambda to pass the device name and entry value
        button = Button(add_window,
                text="OK",
                command=lambda: add_device(device_var.get(), entry))  # Pass the entry widget to get value
        button.grid(row=2, columnspan=2, sticky="nesw")

                            




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
            

        











def run():
    t = SmartHomeApp()
    t.run()

run()
