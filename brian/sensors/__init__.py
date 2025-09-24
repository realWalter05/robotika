from .SensorPort import *
from .BrianBrianComm import *
from .Sensor import *
import sensor_port_probe
import NXT as NXT
import EV3 as EV3
import HiTec as HiTec


class SensorException(Exception):
    """Default sensor Exception"""


class SensorAlreadyClosedError(SensorException):
    """Thrown when trying to access closed Sensor"""


class SensorIsNotReadyError(SensorException):
    """Thrown when trying to read values from a sensor that is not ready"""


class SensorPortAlreadyInUse(SensorException):
    """Thrown when trying to register sensor or sensor probe with autodetect to already used port"""
