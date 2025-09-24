from brian.sensors.Sensor import Sensor
from brian.sensors.SensorPort import SensorPort

class TouchSensorEV3(Sensor):
    """
    Class for interacting with EV3 touch sensor.

    Sensor is automatically registered in the constructor of the base class
    and un-registered in its destructor. It can also be unregistered with the TouchSensorEV3.close_sensor() function.

    There can be at most one instance at any given time, of any sensor class per port in the entire program.
    """
    def __init__(self, port: SensorPort):
        """
        Initialize a EV3 touch sensor at the given port.
        :param port: Sensor port to which the sensor is attached.
        """
        ...

    def is_pressed(self) -> bool:
        """
        Measures the sensor state. Returns boolean of the last button pressed state.
        If the sensor is not ready, returns False.

        :return: True if the sensor button is pressed, False otherwise. Or False if the sensor is not ready.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.
        """
        ...

    def wait_for_press(self, timeout_ms: int = -1) -> bool:
        """
        Waits for next button press event.
        This function is blocking.

        :param timeout_ms: Maximum number of milliseconds to wait. If the timeout is negative, the function will wait indefinitely.

        :return success:
            - True: If the desired button event was caught.
            - False: If the timeout ran out.
        """
        ...

    def wait_for_release(self, timeout_ms: int = -1) -> bool:
        """
        Waits for next button release event.
        This function is blocking.

        :param timeout_ms: Maximum number of milliseconds to wait. If the timeout is negative, the function will wait indefinitely.

        :return success:
            - True: If the desired button event was caught.
            - False: If the timeout ran out.
        """
        ...

    def wait_for_press_and_release(self, timeout_ms: int = -1 ) -> bool:
        """
        Waits for next button press and release event.
        This function is blocking.

        :param timeout_ms: Maximum number of milliseconds to wait. If the timeout is negative, the function will wait indefinitely.

        :return success:
            - True: If the desired button event was caught.
            - False: If the timeout ran out.
        """
        ...
