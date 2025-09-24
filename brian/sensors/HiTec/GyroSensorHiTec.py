from brian.sensors.Sensor import Sensor
from brian.sensors.SensorPort import SensorPort

class GyroSensorHiTec(Sensor):
    """
    Class for interacting with HiTec gyro sensor.

    Sensor is automatically registered in the constructor of the base class
    and un-registered in its destructor. It can also be unregistered with the GyroSensorHiTec.close_sensor() function.

    There can be at most one instance at any given time, of any sensor class per port in the entire program.
    """

    def __init__(self, port: SensorPort):
        """
        Initialize an HiTec gyro sensor at the given port.
        :param port: Sensor port to which the sensor is attached.
        """
        ...

    def speed(self) -> int:
        """
        Measures the sensor state. Returns the angular speed in range -500 to 400

        :return: angular speed in degrees/second (-500 to 400).

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.
        """
        ...
