class AttributeCheck:
    def __init__(self,value,min,max):
        self._value = None
        self.min_val = min
        self.max_val = max
        self.value = value


    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,new_value):
        if not isinstance(new_value,int):
            raise TypeError(f"cant execpt value needs to be type int")
        if not (self.min_val <= new_value <= self.max_val):
            raise ValueError(f"cant execpt value needs to be between {self.min_val} and {self.max_val} is {new_value}")
        self._value = new_value

class SmartDevices:
    def __init__(self,*args):
        if len(args) > 2:
            self._consumption = AttributeCheck(args[0],args[1],args[2])
        self.power = "off"
        self.switch_on = False

    @property
    def consumption(self):
        return self._consumption.value
    
    @consumption.setter
    def consumption(self,new_value):
        self._consumption.value = new_value

    def toggle_switch(self):
        if not isinstance(self.switch_on,bool):
            raise TypeError("wrong type buddy")
        else:
            self.switch_on = not self.switch_on
            if self.switch_on == True:
                self.power = "on"

class SmartPlug(SmartDevices):
    def __init__(self,consumption_rate):
        self.min = 0
        self.max = 150
        super().__init__(consumption_rate,self.min,self.max)

    def __str__(self):
        return f"SmartPlug is {self.power} with a consumption rate of {self.consumption}"

class SmartLight(SmartDevices):
    def __init__(self):
        self.brightness = 50
        self.min = 0
        self.max = 100
        super().__init__(self.brightness,self.min,self.max)

    def __str__(self):
        return f"SmartLight is {self.power} with a consumption rate of {self.consumption}"

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
            raise TypeError("not today buddy")
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
        pass

    def add_device(self,new_device):
        self.device_list.append(new_device)

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






        

def test():
    try:
        plug = SmartDoorBell()
        print(plug)
        plug.toggle_switch()
        plug.sleep_mode = True
        print(plug)
    except (ValueError,TypeError) as error:
        print(f"ik here is error: {error}")


def testhome():
    home = SmartHome()
    plug = SmartPlug(100)
    light = SmartLight()
    doorbell = SmartDoorBell()

    home.add_device(plug)
    home.add_device(light)
    home.add_device(doorbell)

    home.get_device(1) #off

    home.toggle_device(1) 

    home.get_device(1) #on

    home.switch_all_on() 

    home.toggle_device(1) 

    home.get_device(1) #off

    home.toggle_device(1)

    home.switch_all_off() 

    home.get_device(1) #off

    home.toggle_device(1) 

    home.get_device(1) #on

    print(home)

testhome()



