from enum import Enum
from typing import Optional

from brian.sensors.Sensor import Sensor
from brian.sensors.SensorPort import SensorPort


class LightSensorNXT(Sensor):
    """
    Class for interacting with NXT light sensor.

    Sensor is automatically registered in the constructor of the base class
    and un-registered in its destructor. It can also be unregistered with the LightSensorNXT.close_sensor() function.

    There can be at most one instance at any given time, of any sensor class per port in the entire program.
    """

    def __init__(self, port: SensorPort):
        """
        Initialize an NXT light sensor at the given port.
        :param port: Sensor port to which the sensor is attached.
        """
        ...

    def set_led_on(self, led_on: bool) -> None:
        """
        This function sets the sensor to the desired mode. While it’s not mandatory, it is recommended to call this
        function before accessing values from the sensor in a specific mode to prevent SensorIsNotReady exceptions.

        :param led_on: whether the red LED should be set on or off
        """

    def light_value(self, led_on: Optional[bool]) -> float:
        """
        Measures incoming light.

        :param led_on: Indicates whether the red LED should be on or off.
               - If no value is provided or `None` is passed, the previously set LED state will be used.

        :return: Value in range 0-1, with 0 being the darkest and 1 being the brightest.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.
        """
        ...

    def light_value_raw(self, led_on: Optional[bool]) -> int:
        """
        Measures incoming light. Raw measurement is inverted, meaning lower values correspond to brighter light.

        :param led_on: Indicates whether the red LED should be on or off.
               - If no value is provided or `None` is passed, the previously set LED state will be used.

        :return: Value in range 0-4095, with 4095 being the darkest and 0 being the brightest.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.
        """
        ...
