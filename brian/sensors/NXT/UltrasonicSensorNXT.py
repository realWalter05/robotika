from brian.sensors.Sensor import Sensor
from brian.sensors.SensorPort import SensorPort

class UltrasonicSensorNXT(Sensor):
    """
    Class for interacting with NXT ultrasonic sensor.

    Sensor is automatically registered in the constructor of the base class
    and un-registered in its destructor. It can also be unregistered with the UltrasonicSensorNXT.close_sensor() function.

    There can be at most one instance at any given time, of any sensor class per port in the entire program.
    """
    def __init__(self, port: SensorPort):
        """
        Initialize an NXT ultrasonic sensor at the given port.
        :param port: Sensor port to which the sensor is attached.
        """
        ...

    def distance_cm(self) -> int:
        """
        Continuously measures the distance and returns the value in cm.

        :return: distance in cm (0-255).

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.
        """
        ...
