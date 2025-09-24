from .SensorPort import SensorPort
from .sensor_port_probe import AutoDetect


class Sensor:
    """
    Base Sensor class
    """

    def __init__(self, port: SensorPort, sensor_type: AutoDetect):
        """
        Initialize a EV3 sensor class at the given port.
        :param port: Sensor port to which the sensor is attached (sensors.SensorPort.S1-sensors.SensorPort.S4).
        :param sensor_type: Type of the sensor which is attached.

        sensor_port_probe.AutoDetect.ANALOG_P1 corresponds to LightSensorNXT and TouchSensorNXT
        sensor_port_probe.AutoDetect.ANALOG_P6 corresponds to TouchSensor
        sensor_port_probe.AutoDetect.PROTOCOL_UART_EV3 corresponds to ColorSensor, GyroSensor and UltrasonicSensor

        :raises SensorPortAlreadyInUse: When trying to create new sensor on port that is already in use.
        """
        ...

    def __del__(self):
        """
        Deinitialize the sensor and free the port for other uses.
        """
        ...

    def close_sensor(self):
        """
        Deinitialize the sensor and free the port for other uses.
        """
        ...

    def is_connected(self) -> bool:
        """
        :return: True iff sensor is connected and not in the process of rebooting, False otherwise
        """
        ...

    def is_ready(self) -> bool:
        """
        Ready-state indicates that the attempt to read values will give valid results.
        Example reasons for invalid results:
        <ul><li>Sensor is not connected (`is_connected` returns False)</li>
        <li>Sensor is rebooting or not initiated yet</li>
        <li>Sensor is changing modes and the change is not finished yet</li>
        <li>Connected sensor is incompatible with this handler (e.g. wrong type of sensor is connected)</li></ul>
        In all of the above cases, this function will return False.
        :return: True iff values are ready for the next read, False otherwise
        """
        ...

    def wait_until_ready(self, timeout_ms: int = -1) -> bool:
        """
        Waits until the sensor is ready. This function is blocking.
        When changing modes, the sensor enters a "not ready" state for a short period (until
        the mode change is propagated). Therefore, it is recommended to first set the correct
        mode using set_mode() before the calling this function. This only applies to sensors with modes.

        :param timeout_ms: Maximum number of milliseconds to wait. If the timeout is negative, the function will wait indefinitely.

        :return success:
            - True: The sensor is ready.
            - False: The sensor is not ready and time ran out.
        """
        ...

    def reboot(self) -> None:
        """
        Turn off power to the port and turn it back on. This will forcibly reboot the sensor.

        The powered-down state lasts about 100ms. In case of some (mostly digital) sensors, there can be
        some additional time (~1s or more) to boot up and process connection handshake with Brian.
        """
        ...
