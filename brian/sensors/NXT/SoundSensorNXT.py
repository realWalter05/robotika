from brian.sensors.Sensor import Sensor
from brian.sensors.SensorPort import SensorPort

class SoundSensorNXT(Sensor):
    """
    Class for interacting with NXT sound sensor.

    Sensor is automatically registered in the constructor of the base class
    and un-registered in its destructor. It can also be unregistered with the SoundSensorNXT.close_sensor() function.

    There can be at most one instance at any given time, of any sensor class per port in the entire program.
    """
    def __init__(self, port: SensorPort):
        """
        Initialize an NXT sound sensor at the given port.
        :param port: Sensor port to which the sensor is attached.
        """
        ...

    def sound_intensity(self) -> float:
        """
        Measures incoming sound.

        :return: Value in range 0-1, with 0 being the quietest and 1 being the loudest.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.
        """
        ...

    def sound_intensity_raw(self) -> int:
        """
        Measures incoming sound. Raw measurement is inverted, meaning lower values correspond to louder sounds.

        :return: Value in range 0-4095, with 4095 being the quietest and 0 being the loudest.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.
        """
        ...
