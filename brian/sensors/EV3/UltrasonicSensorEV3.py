from enum import Enum
from brian.sensors.Sensor import Sensor
from brian.sensors.SensorPort import SensorPort

class UltrasonicSensorEV3(Sensor):
    """
    Class for interacting with EV3 ultrasonic sensor.

    Sensor is automatically registered in the constructor of the base class
    and un-registered in its destructor. It can also be unregistered with the UltrasonicSensorEV3.close_sensor() function.

    There can be at most one instance at any given time, of any sensor class per port in the entire program.
    """
    def __init__(self, port: SensorPort):
        """
        Initialize a EV3 ultrasonic sensor at the given port.
        :param port: Sensor port to which the sensor is attached.
        """
        ...


    class Mode(Enum):
        """"""
        DISTANCE_MM = 0
        """"""
        DISTANCE_TENTHS_OF_INCH = 1
        """"""
        DETECT_OTHER_US = 2
        """"""
        SINGLESHOT_MM = 3
        """"""
        SINGLESHOT_TENTHS_OF_INCH = 4
        """"""

    def set_mode(self, mode: Mode) -> None:
        """
        This function sets the sensor to the desired mode. While it’s not mandatory, it is recommended to call this
        function before accessing values from the sensor in a specific mode to prevent SensorIsNotReady exceptions.

        :param mode: desired mode to be set
        """

    def distance_mm(self) -> int:
        """
        Sets the sensor mode to `DISTANCE_MM` and return the last value.

        :return: distance in mm (0-2550). Or 2550 it reported a measurement error.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.

        <b>DISTANCE_MM mode:</b>
        Continuously measures the distance and returns the value in mm.
        Returns the last measured distance in mm, in range 0-2550. If the measurement fails, the
        sensor reports a magic number (distance) of 2550.
        """
        ...

    def distance_tenths_of_inch(self) -> int:
        """
        Sets the sensor mode to `DISTANCE_TENTHS_OF_INCH` and return the last value.

        :return: distance in tenths of an inch (0-1003).

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.

        <b>DISTANCE_TENTHS_OF_INCH mode:</b>
        Continuously measures the distance and returns the value in tenths of an inch.
        Returns the last measured distance in tenths of an inch, in range 0-1003. If the measurement fails, the
        sensor reports a magic number (distance) of 1003.
        distance_tenths_of_inch
        """
        ...

    def last_single_shot_mm(self) -> int:
        """
        If the sensor is in `SINGLESHOT_MM` mode, returns the last value.
        If the sensor is in a different mode returns 2550. This method
        does not trigger the measurement. To trigger the measurement, use trigger_single_shot_measurement_mm().

        :return: distance in mm (0-2550). Or 2550 if it reported a measurement error.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.

        <b>SINGLESHOT_MM mode:</b>
        Activates once and measures the distance. After the measurement, the sensor goes to sleep and
        does not produce ultrasonic waves. This mode can be used when handling multiple ultrasonic
        sensors at the same time, to avoid interference between them. The single shot mode should not
        be called more often than about once in 250ms.
        Returns the last measured distance in mm, in range 0-2550. If the measurement fails, the
        sensor reports a magic number (distance) of 2550.
        """
        ...

    def trigger_single_shot_measurement_mm(self) -> None:
        """
        Sets the sensor mode to `SINGLESHOT_MM` and triggers the measurement.
        Does not wait for the result and does not return anything.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.

        <b>SINGLESHOT_MM mode:</b>
        Activates once and measures the distance. After the measurement, the sensor goes to sleep and
        does not produce ultrasonic waves. This mode can be used when handling multiple ultrasonic
        sensors at the same time, to avoid interference between them. The single shot mode should not
        be called more often than about once in 250ms.
        Returns the last measured distance in mm, in range 0-2550. If the measurement fails, the
        sensor reports a magic number (distance) of 2550.
        """
        ...

    def last_single_shot_tenths_of_inch(self) -> int:
        """
        If the sensor is in `SINGLESHOT_TENTHS_OF_INCH` mode, returns the last value.
        If the sensor is in a different mode, returns 1003. This method
        does not trigger the measurement. To trigger the measurement, use trigger_single_shot_measurement_tenths_of_inch()

        :return: distance in tenths of an inch (0-1003). Or 1003 if it reported a measurement error.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.

        <b>SINGLESHOT_TENTHS_OF_INCH mode:</b>
        Activates once and measures the distance. After the measurement, the sensor goes to sleep and
        does not produce ultrasonic waves. This mode can be used when handling multiple ultrasonic
        sensors at the same time, to avoid interference between them. The single shot mode should not
        be called more often than about once in 250ms.
        Returns the last measured distance in tenths of an inch, in range 0-1003. If the measurement fails, the
        sensor reports a magic number (distance) of 1003.
        last_single_shot_tenths_of_inch
        """
        ...

    def trigger_single_shot_measurement_tenths_of_inch(self) -> None:
        """
        Sets the sensor mode to `SINGLESHOT_TENTHS_OF_INCH` and triggers the measurement.
        Does not wait for the result and does not return anything.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.

        <b>SINGLESHOT_TENTHS_OF_INCH mode:</b>
        Activates once and measures the distance. After the measurement, the sensor goes to sleep and
        does not produce ultrasonic waves. This mode can be used when handling multiple ultrasonic
        sensors at the same time, to avoid interference between them. The single shot mode should not
        be called more often than about once in 250ms.
        """
        ...

    def is_other_us_detected(self) -> bool:
        """
        Sets the sensor mode to `DETECT_OTHER_US` and return the last value.


        :return: True if other ultrasonic sensor is active and in range, False otherwise.

        :raises brian.sensors.SensorIsNotReadyError: If the sensor is not ready.

        <b>DETECT_OTHER_US mode:</b>
        Check if another ultrasonic sensor is active within the hearing distance of this sensor.
        Returns boolean value - True indicates that another ultrasonic sensor has been detected.
        A true value can also be triggered by a loud noise such as clapping.
        """
        ...
