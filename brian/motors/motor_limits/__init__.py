UNLIMITED_ACCELERATION: int
"""Maximum available acceleration limit (disables speed ramping)"""
UNLIMITED_TORQUE: int
"""Maximum available torque limit"""
UNLIMITED_POWER: int
"""Maximum available power limit"""

class MotorLimits:
    """
    A class to manage and configure the limits of a motor.
    """

    @property
    def battery_power(self) -> int:
        """
        Query the power draw limit.

        :return: Battery power consumption limit, in milli-watts.
        """
        ...

    @battery_power.setter
    def battery_power(self, mW: int) -> None:
        """
        Set the power draw limit.

        :param mw: Maximum power allowed to draw from the battery, in milli-watts.
        """
        ...

    @property
    def torque(self) -> int:
        """
        Query the torque limit.

        :return: Maximum torque that will be applied to the motor axle, in milli-newton-meters.
        """
        ...

    @torque.setter
    def torque(self, mNm: int) -> None:
        """
        Set the torque limit.

        :param mNm: Maximum torque that will be applied to the motor axle, in milli-newton-meters.
        """
        ...

    @property
    def acceleration(self) -> int:
        """
        Query the maximum acceleration limit.

        :return: Maximum acceleration in degrees per second squared.
        """
        ...

    @acceleration.setter
    def acceleration(self, deg_per_sec_sq: int) -> None:
        """
        Set the maximum acceleration limit.

        :param deg_per_sec_sq: Maximum acceleration in degrees per second squared.
        """
        ...
