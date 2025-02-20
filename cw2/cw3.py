class AttributeCheck:
    def __init__(self,min,max,value):
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
        else:
            self.switch_case_2 = args[1]

        self.switch_case = args[3]
        self.power = "off"

    @property
    def consumption(self):
        return self._consumption.value
    
    @consumption.setter
    def consumption(self,new_value):
        self._consumption.value = new_value

    def toggle_switchs(self,switch):
        if not isinstance(switch,bool):
            raise TypeError("wrong type buddy")
        else:
            switch = not switch
            if switch == True:
                self.power = "on"
    def toggle_switch(self):
        self.toggle_switchs()

class SmartPlug(SmartDevices):
    def __init__(self,consumption_rate):
        self.min = 0
        self.max = 150
        self.switch_on = False
        super().__init__(consumption_rate,self.min,self.max,self.switch_on)

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
        self.sleep_mode = False
        self.switch_on = False
        super().__init__(self.sleep_mode,self.switch_on)

    def __str__(self):
        return f"hello im working"








        

def test():
    try:
        plug = SmartPlug(100)
        print(plug)
        plug.toggle_switch()
        plug.consumption = 125
        print(plug)
    except (ValueError,TypeError) as error:
        print(f"ik here is error: {error}")


test()


