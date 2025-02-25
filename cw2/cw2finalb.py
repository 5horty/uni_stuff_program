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
            raise TypeError("wrong type buddy")
        else:
            self._switch_on = new_value
            if self._switch_on: self.power = "on"

    @property
    def option(self):
        return self._option

    @option.setter
    def option(self,new_value):
        if not isinstance(new_value,int):
            raise TypeError(f"cant execpt value needs to be type int")
        if not (self.min_val <= new_value <= self.max_val):
            raise ValueError(f"cant execpt value needs to be between {self.min_val} and {self.max_val} is {new_value}")
        self._option = new_value

    def toggle_switch(self):
        self._switch_on = not self._switch_on
        if self._switch_on == True:
            self.power = "on"

class SmartPlug(SmartDevices):
    def __init__(self,consumption_rate):
        self.min = 0
        self.max = 150
        super().__init__(consumption_rate,self.min,self.max)

    def __str__(self):
        return f"SmartPlug is {self.power} with a consumption rate of {self.option}"

class SmartLight(SmartDevices):
    def __init__(self):
        self._brightness = 50
        self.min = 0
        self.max = 100
        super().__init__(self._brightness,self.min,self.max)

    def __str__(self):
        return f"SmartLight is {self.power} with a consumption rate of {self.option}"

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
        self.max_items = 10

    def add_device(self,new_device):
        if len(self.device_list) < 10:
            self.device_list.append(new_device)
        else:
            raise IndexError("too many items")
    
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
        else:
            raise AttributeError("not an attribute")

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
    light.switch_on = True
    doorbell = SmartDoorBell()
    try:
        home.add_device(plug)
        home.add_device(light)
        home.add_device(doorbell)
        print(home)


#        home.get_device(1) #off

 #       home.toggle_device(1) 

  #      home.get_device(1) #on

        home.switch_all_on() 

   #     home.toggle_device(1) 

    #    home.get_device(1) #off

     #   home.toggle_device(1)

      #  home.switch_all_off() 

       # home.get_device(1)   # off

        #home.toggle_device(1) 

        #home.get_device(1)  #on

        #home.update_option(0,75)
        #home.update_option(2,True)

        print(home)
    except (TypeError,ValueError,IndexError,AttributeError) as error:
        print(f"error=> {error}")

if __name__ == "__main__":
    testhome()




