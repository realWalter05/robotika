from typing import List
from enum import Enum
from brian.sensors.SensorPort import SensorPort as SensorPort


class AutoDetect(Enum):
    """"""
    NOT_CONNECTED = 1 << 6,
    """"""

    ANALOG_P1 = 0b00,
    """"""
    ANALOG_P1_HACKER = 0b100
    """ Force P1 ADC mode, regardless of what AD thinks"""
    ANALOG_P6 = 0b10,
    """"""
    ANALOG_P6_HACKER = 0b110
    """ Force P6 ADC mode, regardless of what AD thinks"""

    I2C_9K6 = 0b0011
    """ NXT ultrasonic uses bit banging I2C implementation and cannot operate faster than 9600 bits/s"""
    I2C_100K = 0b0111
    """ Some other 3rd party sensors may support only standard I2C speed"""
    I2C_400K = 0b1011
    """ Most other 3rd party sensors support fast I2C speeds"""
    UART_2400 = 0b0001
    """"""
    UART_9600 = 0b0101
    """"""
    UART_115K = 0b1001
    """ 115200 baud"""
    UART_MULTI_BRIAN_MASTER = UART_115K + (1 << 5)
    """"""
    UART_MULTI_BRIAN_SLAVE = UART_115K + (1 << 5) + (1 << 4)
    """ Slave has uart RX/TX pins swapped"""

    PROTOCOL_UART_EV3 = UART_2400 + (1 << 4)
    """"""
    PROTOCOL_I2C_NXT_REG = I2C_9K6 + (1 << 4)
    """"""

    ERROR = 1 << 7, """ MSB is error flag, the rest can be used as an error code"""
    """"""

class SensorInfo:
    """
    i2c protocol specifies type as 8char string; uart ev3 as a single byte 0-255 when uart ev3 protocol is used,
    the name can be something like: "Uart 39" and the code will contain the actual value when i2c protocol is used,
    the code can be = 0
    """

    @property
    def sensor_type_name(self) -> str:
        """ The sensor type name as a string. """
        ...

    @property
    def sensor_type_code(self) -> int:
        """ Represents the sensor type code. """
        ...

    @property
    def selected_mode(self) -> int:
        """ The currently selected mode of the sensor. """
        ...

    @property
    def mode_name(self) -> str:
        """ The name of the current mode. """
        ...

    @property
    def mode_count(self) -> int:
        """
        Set by sensor handler. EV3 sensors report their mode count. Generic I2C sensor will have 0.
        Specific I2C sensors (NXT US) will have constant mode count. Even analog sensor, such as NXT light can have
        multiple modes and mode count - active, passive, blinking differential handled by ST code
        """
        ...

    @property
    def unit_name(self) -> str:
        """ Name of the measurement unit. """
        ...

    @property
    def raw_min(self) -> float:
        """ Minimum raw sensor value. """
        ...

    @property
    def raw_max(self) -> float:
        """ Maximum raw sensor value. """
        ...

    @property
    def pct_min(self) -> float:
        """ Percent value corresponding to the minimum raw value. """
        ...

    @property
    def pct_max(self) -> float:
        """ Percent value corresponding to the maximum raw value. """
        ...

    @property
    def si_min(self) -> float:
        """ Scaled International (SI) value corresponding to the minimum raw value. """
        ...

    @property
    def si_max(self) -> float:
        """ Scaled International (SI) value corresponding to the maximum raw value. """
        ...

class SensorPortProbe:
    """"""
    is_sensor_api_handler_registered: bool
    """"""

    is_connected: bool
    """"""
    auto_detect: AutoDetect
    """"""
    auto_detect_hint: AutoDetect
    """"""

    info: SensorInfo
    """"""


def probe_sensor(port: SensorPort) -> SensorPortProbe:
    """
    Return latest read-only information about a sensor connected to a given port. This method can be called
    any time (regardless of registered Sensor port handler or if it is not registered)
    :param port: sensor port to probe.
    :return: information about the current port usage
    """
    ...


def probe_sensor_with_autodetect_hint(port: SensorPort, hint: AutoDetect) -> SensorPortProbe:
    """
    Return latest read-only information about a sensor connected to a given port.
    It requests a specific handling of the sensor, based on the autodetect hint.
    The hint may be used to initialize a specific software protocol over a detected bus
    (e.g. use EV3 UART protocol if the detected sensor interfaces using UART).
    When you expect a specific class of sensors to be connected, this may be useful to
    extract more information, for example about the sensor modes.
    This method can be used only, when there is no Sensor handler registered.
    :param port: sensor port to probe.
    :param hint: hint to for autodetect (e.g. software protocol over detected hw bus)
    :return: information about the current port usage

    :raises SensorPortAlreadyInUse: When trying to probe port that is already in use.
    """
    ...


def reboot(port: SensorPort) -> None:
    """
    Turn off power to the port and turn it back on. This will forcibly reboot the sensor.
    The powered-down state lasts about 100ms. In case of some (mostly digital) sensors, there can be
    some additional time (~1s or more) to boot up and process connection handshake with Brian.
    This method can be used only, when there is no Sensor handler registered. When there is, use the method
    in the Sensor handler itself.
    :param port: sensor port to force reboot.
    """
    ...
