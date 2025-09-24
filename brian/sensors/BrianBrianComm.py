from brian.sensors.Sensor import Sensor
from brian.sensors.SensorPort import SensorPort
from typing import Optional, Union


class BrianBrianComm(Sensor):
    """
    Class exposing the communication between two Brians connected via a sensor port.

    Sensor (other Brian) is automatically registered in the constructor of the base class
    and un-registered in its destructor.

    There can be at most one instance at any given time, of any sensor class per port in the entire program.
    """

    def __init__(self, port: SensorPort, is_master: bool) -> None:
        """
        Initialize a new Brian-Brian communication handler at the given port.
        The communication can be initialized in either of two modes - master and slave.
        One of the ends must be master, the other must be slave.

        :param port: Sensor port to which the sensor is attached.
        :param is_master: true if this should be used in master mode, false for slave mode
        """
        ...
    def available(self) -> int:
        """
        :return: bytes available to be read
        """
        ...

    def read(self, size: Optional[int] = None ) -> bytes:
        """
        reads data incoming from the other Brian.

        :param size: size limit, how many bytes to copy. If not provided, all available data will be read.
        :return: read bytes

        :raises OSError: If an error occurs during the write operation.
        <br>**Error Codes:**<ul>
            <li>`MP_EIO`: BrianBrianComm is not ready or is disconnected.</li>
        </ul>
        """
        ...

    def write(self, message: Union[bytearray, str, bytes]) -> int:
        """
        Sends the given buffer to the other Brian.

        :param message: str, bytearray or bytes buffer containing the actual message.

        :return: number of bytes written

        :raises OSError: If an error occurs during the write operation.
        <br>**Error Codes:**<ul>
            <li>`MP_EIO`: BrianBrianComm is not ready or is disconnected.</li>
        </ul>

        """
        ...
