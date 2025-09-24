from .MotorPort import MotorPort
from .Motor import Motor


class NXTMotor(Motor):
    def __init__(self, port: MotorPort):
        """
        Initialize a new NXTMotor motor object on the given port.

        This constructor does not fail if the motor is not connected yet.

        :param port: Motor port to use.
        """
        ...
