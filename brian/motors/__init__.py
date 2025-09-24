from MotorPort import *
from Motor import *
from EV3LargeMotor import *
from EV3MediumMotor import *
from NXTMotor import *
from MovementEnd import *
import motor_types
import motor_port_probe
import motor_limits


class MotorException(Exception):
    """Default motor Exception"""


class MotorAlreadyClosedError(MotorException):
    """Thrown when trying to access closed Motor"""


class MotorInitializationFailedError(MotorException):
    """Thrown when motor initialization fails during innit"""


class MotorPortAlreadyInUse(MotorException):
    """Thrown when trying to register motor or motor probe with port mode to already used port"""
