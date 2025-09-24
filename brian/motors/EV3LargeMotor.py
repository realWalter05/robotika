from .MotorPort import MotorPort
from .Motor import Motor


class EV3LargeMotor(Motor):
    """
    A class to manage and control EV3LargeMotor operations.
    """

    def __init__(self, port: MotorPort):
        """
        Initialize a new EV3LargeMotor motor object on the given port.

        This constructor does not fail if the motor is not connected yet.

        :param port: Motor port to use.
        """
        ...
