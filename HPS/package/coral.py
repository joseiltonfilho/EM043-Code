from package.sensorcontroller import *
from package.utility import *

class coral(SensorController):
    def __init__(self,name="coral", real=False, offset=0x0) -> None:
        self.name = name
        self.modules = {
            'pixel'         : 0, #Sensor('pixel',            'float',real,       offset)
            'heath_status'  : 'ok'
        }
        
    def get_telemetries(self,bridge):
        data = {}
        data[self.name] = {"pixel": bridge, "heath_status": "-"}
        return data