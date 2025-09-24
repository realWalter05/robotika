from typing import Optional
from .motor_limits import MotorLimits
from .MotorPort import MotorPort
from .MovementEnd import MovementEnd
from .motor_types import MotorType


class Motor:
    """
    A class to manage and control motor operations.
    """

    @property
    def limits(self) -> 'MotorLimits':
        """
        Configure various controller limits.

        :return: MotorLimits object that can be used for configuring the limits.
        """
        ...

    @property
    def motor_type(self) -> 'MotorType':
        """
        Check what motor type was this object initialized with.

        :return: Properties and default settings of the connected motor type.
        """
        ...

    def __init__(self, port: MotorPort):
        """
        Tries to autodetect a motor, connected to the given port and initialize a new motor class.
        :raises MotorInitializationFailedError: If autodetect fails (motor is not connected, unknown type of the connected motor).

        :param port: Motor port to use.

        :raises MotorPortAlreadyInUse: When trying to create new Motor on a port that is already in use.
        """
        ...

    def __del__(self):
        """
        Release the motor port for other uses.
        """
        ...

    def close_motor(self):
        """
        Release the motor port for other uses.
        """
        ...

    def is_connected(self) -> bool:
        """
        Check if something is connected to the port.

        :return: True if a non-empty port was detected; False otherwise.
        """
        ...

    def is_ready(self) -> bool:
        """
        Check if a correct motor is connected to the port and is ready to be controlled.

        Test for `is_connected` is done internally, if it returns false, `is_ready` will always return false.

        :return: True if a motor is connected, and it is the correct type; False otherwise.
        """
        ...

    def wait_until_ready(self, timeout_ms: Optional[int] = None) -> bool:
        """
        Waits until the motor is ready. This function is blocking.

        :param timeout_ms: Maximum number of milliseconds to wait.
            - If the timeout is not provided or is None, the function will wait indefinitely.

        :return success:
            - True: The sensor is ready.
            - False: The sensor is not ready and timeout ran out.
        """
        ...

    def current_angle(self) -> int:
        """
        Query the current motor angle.

        :return: Motor axle angle in degrees.
        """
        ...

    def reset_angle(self, new_value: int = 0) -> None:
        """
        Set the accumulated angle to the provided position.

        Assuming that the motor will not move, current_angle() will
        start returning the value in newValue.

        :param new_value: New motor position in degrees.
        """
        ...

    def current_speed(self) -> int:
        """
        Query the current motor rotational speed.

        :return: Motor axle speed in degrees/second.
        """
        ...

    def current_torque(self) -> int:
        """
        Query the current estimated motor torque.

        :return: Motor torque in milli-newton-meters.
        """
        ...

    def is_stalled(self) -> bool:
        """
        Check if the motor is currently stalled.

        :return: True if the motor is exceeding some limit, False otherwise.
        """
        ...

    def coast(self) -> None:
        """
        Let the motor spin freely.

        This will float the motor windings.
        """
        ...

    def brake(self) -> None:
        """
        Passively brake the motor.

        This will short the motor windings.
        """
        ...

    def hold(self) -> None:
        """
        Actively brake the motor at the current position.

        This will actively control the motor to stay at the current position.
        """
        ...

    def run_unregulated(self, fraction: float) -> None:
        """
        Run the motor at a given fraction of the maximum available voltage.

        :param fraction: Value between -1.0 and +1.0 that determines the duty cycle.
        """
        ...

    def run_at_voltage(self, volts: float) -> None:
        """
        Run the motor at the given voltage.

        :param volts: Desired voltage on the motors, in volts. Useful range is
                      -battery voltage to +battery voltage (this is cca. -8V to +8V).
                      The maximum range accepted by this function is -12V to +12V.
        """
        ...

    def run_at_speed(self, deg_per_sec: int) -> None:
        """
        Run the motor at a constant speed.

        :param deg_per_sec: Desired rotational speed, in degrees per second.
        """
        ...

    def rotate_by_angle(self, angle: int, speed: int, timeout: Optional[int] = None) -> 'MovementEnd':
        """
        Turn the motor to a new position, relative to the current position.

        :param angle: Angle to rotate by, in degrees.
        :param speed: Speed to use for the maneuver, in degrees per second.
                      If the provided speed is negative, absolute value is used.
        :param timeout: How long to wait for the maneuver to complete, in milliseconds.
                        If zero, the function will return immediately.
                        If the timeout expires, the motor is not stopped.
        :return: Whether the wait-for-end was successful or why it ended, if it ended early.
        """
        ...

    def rotate_to_angle(self, position: int, speed: int, timeout: Optional[int] = None) -> 'MovementEnd':
        """
        Turn the motor to a new position, relative to the zero position.

        :param position: Angle to rotate to, in degrees.
        :param speed: Speed to use for the maneuver, in degrees per second.
                      If the provided speed is negative, absolute value is used.
        :param timeout: How long to wait for the maneuver to complete, in milliseconds.
                        If zero, the function will return immediately.
                        If the timeout expires, the motor is not stopped.
        :return: Whether the wait-for-end was successful or why it ended, if it ended early.
        """
        ...

    def rotate_to_angle_without_speed_control(self, position: int) -> None:
        """
        Try to get as fast as possible to the specified position.

        This will ignore any speed and acceleration limits - you must provide these
        yourself by periodically calling this function with new positions.

        :param position: Angle to rotate to relative to the zero position, in degrees.
        """
        ...

    def movement_done(self) -> bool:
        """
        Check whether the last invoked position command has completed.

        :return: True if the motor has reached the goal.
                 True if the maneuver had to be interrupted (e.g., motor was unplugged).
                 False if the motor is still moving.
        """
        ...

    def wait_for_movement(self, timeout_ms: Optional[int] = None) -> 'MovementEnd':
        """
        Wait for the motor to complete the last position command.

        :param timeout_ms: How long to wait for the maneuver to complete, in milliseconds.
                        If zero, the function will return immediately.
                        If the timeout expires, the motor is not stopped.
        :return: Whether the wait-for-end was successful or why it ended, if it ended early.
        """
        ...
