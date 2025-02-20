


class SmartDevices:
    def __init__(self,value):
        self._option_attribute = None
        self.option_attribute = value
        self.switched_on = False

    @property
    def option_attribute(self):
        return self._option_attribute

    @option_attribute.setter
    def option_attribute(self,new_value):
        if not (0 <= new_value <= 150):   
            raise ValueError(f"value needs to be a number between 0-150 is {new_value}")
        self._option_attribute = new_value


    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def __str__(self):
        power = "off"
        if self.switched_on == True:
            power = "on"
        return f"SmartPlug is {power} with a consumption rate of {self.consumption_rate}"







class SmartPlug:
    def __init__(self,consumption_rate:int):
        self._consumption_rate = None
        self.consumption_rate = consumption_rate
        self.switched_on = False

    @property
    def consumption_rate(self):
        return self._consumption_rate
    
    @consumption_rate.setter
    def consumption_rate(self,new_consumption_rate):
        if not (0 <= new_consumption_rate <= 150):   
            raise ValueError(f"value needs to be a number between 0-150 is {new_consumption_rate}")
        self._consumption_rate = new_consumption_rate


    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def __str__(self):
        power = "off"
        if self.switched_on == True:
            power = "on"
        return f"SmartPlug is {power} with a consumption rate of {self.consumption_rate}"


def test_smart_plug():
    try:
        t = SmartPlug(45)
        print(t)
        t.toggle_switch()
        print(t)
        t.consumption_rate = 75
        print(t)
        t.toggle_switch()
        print(t)
    except Exception as error:
        print(f"unexpected error: {error}")
    
    for i in [-10,200]:
        try:
            t.consumption_rate = i
        except ValueError as error:
            print(f"{error} and here is unchanged {t}")
    for j in [-5,160]:
        try:
            plug = SmartPlug(i)
        except ValueError as error:
            print(f"here is error: {error}")
    

class 
