import os
import json
from re import I

class SmartDevices:
    def __init__(self,*args):
        if len(args) > 2:
            self._option = None
            self.min_val = args[1]
            self.max_val = args[2]
            self.option = args[0]
        self.power = "off"
        self._switch_on = False

    @property
    def switch_on(self):
        return self._switch_on

    @switch_on.setter
    def switch_on(self,new_value):
        if not isinstance(new_value,bool):
            raise TypeError("error wrong type was entered")
        else:
            self._switch_on = new_value
            if self._switch_on: 
                self.power = "on"
            else:
                self.power = "off" 

    @property
    def option(self):
        return self._option

    @option.setter
    def option(self,new_value):
        if not isinstance(new_value,(int,bool,str)):
            raise TypeError(f"cant execpt value needs to be type int")
        if not (self.min_val <= new_value <= self.max_val):
            raise ValueError(f"cant execpt value needs to be between" 
                        + f"{self.min_val} and {self.max_val} is {new_value}")
        self._option = new_value

    def toggle_switch(self):
        self.switch_on = not self.switch_on
        if self._switch_on == True:
            self.power = "on"

class SmartPlug(SmartDevices):
    def __init__(self,consumption_rate):
        self.min = 0
        self.max = 150
        super().__init__(consumption_rate,self.min,self.max)

    def __str__(self):
        output = f"SmartPlug is {self.power}" 
        output += f" with a consumption rate of {self.option}"
        return output

class SmartLight(SmartDevices):
    def __init__(self):
        self._brightness = 50
        self.min = 0
        self.max = 100
        super().__init__(self._brightness,self.min,self.max)

    def __str__(self):
        return f"SmartLight is {self.power} with a brightness of {self.option}"

class SmartDoorBell(SmartDevices):
    def __init__(self):
        self._sleep_mode = False
        super().__init__()
    
    @property
    def sleep_mode(self):
        return self._sleep_mode

    @sleep_mode.setter
    def sleep_mode(self,new_value):
        if not isinstance(new_value,bool):
            raise TypeError("error please enter a valid setting")
        else:
            self._sleep_mode = new_value
         
    def __str__(self):
        sleep = "off"
        if self._sleep_mode:
            sleep = "on"
        return f"SmartDoorBell is {self.power} and sleep mode is {sleep}"

class SmartHome:
    device_list = []
    def __init__(self):
        self.max_items = 10

    def add_device(self,new_device):
        if len(self.device_list) < 10:
            self.device_list.append(new_device)
        else:
            raise IndexError("limit is exceeded too many devices")
    
    def remove_device(self,index):
        if (index <= 10) and (index >= 0):
            self.device_list.pop(index)
        else:
            raise IndexError("index not valid")
        
    def update_option(self,index,value):
        if not (index <= 10) and (index >= 0):
            raise IndexError("index not valid")
        elif not hasattr(self.device_list[index],"option"):
            self.device_list[index].sleep_mode = value
        elif hasattr(self.device_list[index],"option"):
            self.device_list[index].option = value

    def get_device(self,index):
        return self.device_list[index]
    
    def toggle_device(self,index):
        self.device_list[index].toggle_switch()

    def switch_all_on(self):
        for device in self.device_list:
            device.switch_on = True

    def switch_all_off(self):
        for device in self.device_list:
            device.switch_on = False

    def __str__(self):
        output = f"SmartHome with {len(self.device_list)} device(s) \n"
        for index in range(len(self.device_list)):
            output += f"{index+1}  {self.device_list[index]}  \n" 
        return output

#chal not working


class SmartHomesApp:
    def __init__(self,file_name = "Smart_home.json"):
        self.file_name = file_name
        self.homes = self.load_homes()


    def load_homes(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name,"w") as file:
                json.dump({},file)
            return {}
        try:
            with open(self.file_name,"r") as file:
                return json.load(file)
        except (json.JSONDecodeError,FileNotFoundError) as e:
            return {}

    def save_homes(self):
        with open(self.file_name,"w") as file:
            json.dump(self.homes,file)


    def add_home(self,home):
        self.homes[len(self.homes.keys())+1] = {"devices":[
        {"type": device.__class__.__name__,"attr":device.__dict__}  
        for device in home.device_list]}
        self.save_homes()

    def remove_home(self, index):
        if index not in self.homes:
            raise ValueError("Home not found.")
        del self.homes[index]
        self.save_homes()

    def list_homes(self):
        return list(self.homes.keys())

    def get_home(self, index):
        if index not in self.homes:
            raise ValueError("Home not found.")
        return self.homes[index]

def test_smart_plug():
    plug = SmartPlug(45)
    print(plug)
    plug.toggle_switch()
    print(plug)
    plug.option = 75 
    plug.toggle_switch()
    print(plug)
    for i in [-10,200]:
        try:
            plug.option = i
        except ValueError as e:
            print(f"{e}")

    for j in [-5,160]:
        try:
            plug2 = SmartPlug(j)
        except ValueError as e:
            print(f"{e}")

def test_custom_device():
    doorbell = SmartDoorBell()
    light = SmartLight()

    print(light)
    print(doorbell)

    doorbell.toggle_switch()
    light.toggle_switch()

    print(light)
    print(doorbell)

    doorbell.sleep_mode = True
    light.option = 69

    print(light)
    print(doorbell)
    
    try:
        doorbell.sleep_mode = 69420
    except (ValueError,TypeError) as e:
        print(f"{e}")

    try:
        light.option = 42069
    except (ValueError,TypeError) as e:
        print(f"{e}")

def test_smart_home():
    plug = SmartPlug(45)
    light = SmartLight()
    doorbell = SmartDoorBell()

    home = SmartHome()
    home.add_device(plug)
    home.add_device(light)
    home.add_device(doorbell)

    print(home)

    print(home.get_device(1))

    home.toggle_device(0)
    home.toggle_device(1)
    home.toggle_device(2)

    print(home)

    home.switch_all_on()
    print(home)
    home.switch_all_off()
    print(home)

    try:
        for i in range(69):
            device = SmartDoorBell()
            home.add_device(device)
    except IndexError as e:
        print(f"{e}")

    home.device_list = []

    home.add_device(plug)
    home.add_device(light)
    home.add_device(doorbell)
    
    home.remove_device(0)
    print(home)
    for i in [-1,69]:
        try:
            home.remove_device(i)
        except (IndexError) as e:
            print(f"{e}")

    home.update_option(0,100)
    home.update_option(1,True)

    print(home)

    for i in range(2):
        try:
            home.update_option(i,42069)
        except (ValueError,TypeError) as e:
            print(f"{e}")

    print(home)


if __name__ == "__main__":
    pass
#test_custom_device()
#test_smart_home()
#test_smart_plug()

