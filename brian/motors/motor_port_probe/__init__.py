from typing import List
from enum import Enum
from brian.motors.MotorPort import MotorPort as MotorPort
from brian.motors.motor_types import DeviceClass as DeviceClass
from brian.motors.motor_types import DeviceType as DeviceType


class AutoDetect:
    """"""

    def __init__(self, device_class: DeviceClass, device_type: DeviceType):
        """"""
        ...

    @property
    def device_class(self) -> DeviceClass:
        """Detected device class (PortMode must not be POWER_OFF)"""
        ...

    @property
    def device_type(self) -> DeviceType:
        """More detailed device type"""
        ...


class PortMode(Enum):
    """"""
    POWER_OFF = 0
    """Disabled state"""
    AUTOID_ONLY = 1
    """Passive probing state"""
    ANALOG_MOTOR = 2
    """NXT/EV3 motor"""


class MotorPortProbe:
    """"""

    is_motor_api_handler_registered: bool
    """"""
    is_connected: bool
    """"""
    auto_detect: 'AutoDetect'
    """"""
    port_mode: 'PortMode'
    """"""


def probe_motor(port: 'MotorPort') -> 'MotorPortProbe':
    """
    Return latest read-only information about a motor connected to a given port. This method can be called
    any time (regardless of registered Motor port handler or if it is not registered)

    :param port: port motor port to probe.
    :return: information about the current port usage
    """
    ...


def probe_motor_with_port_mode_hint(port: 'MotorPort', hint: 'PortMode') -> 'MotorPortProbe':
    """
    Return latest read-only information about a motor connected to a given port. It requests a specific mode of the
    port, based on the provided PortMode. The hint may be used to initialize a specific software protocol over a
    detected bus (e.g. use EV3 UART protocol if the detected motor interfaces using UART). When you expect a specific
    class of motors to be connected, this may be useful to extract more information, for example about supported
    behavior. This method can be used only, when there is no Motor handler registered.

    :param port: port motor port to probe.
    :param hint: PortMode target port mode. Only 'PortMode.POWER_OFF' and 'PortMode.AUTOID_ONLY' can be set manually.
    :return: information about the current port usage

    :raises MotorPortAlreadyInUse: When trying to create probe port that is already in use.
    """
    ...
