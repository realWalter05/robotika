from enum import Enum

class DeviceClass(Enum):
    """"""

    NONE = 0
    """"""
    ERROR = 1
    """"""
    EV3_ANALOG_MOTOR = 2
    """"""
    EV3_UART_DEVICE = 3
    """"""


class DeviceType(Enum):
    """"""
    UNKNOWN = 0
    """"""
    NXT_EV3_LARGE_MOTOR = 7
    """"""
    EV3_MEDIUM_MOTOR = 8
    """"""
class MotorType:

    @property
    def name(self) -> str:
        """
        :return: Human-readable name of the motor
        """
        ...

    @property
    def identification(self) -> 'Identification':
        """
        :return: What will Brian report as the ID when this motor is connected
        """
        ...

    @property
    def default_constants(self) -> 'DefaultConstants':
        """
        :return: Default controller configuration
        """
        ...

    @property
    def default_acceleration_limit(self) -> int:
        """"""
        ...

    class Identification:
        """
        Results of auto-detection
        """
        @property
        def device_type(self) -> 'DeviceClass':
            """
            :return: Detected device class (portMode must not be POWER_OFF)
            """
            ...

        @property
        def device_class(self) -> 'DeviceType':
            """
            :return: More detailed device type
            """
            ...

    class DefaultConstants:
        """
        Control loop parameters that are typically not changed much
        """
        @property
        def motor(self) -> 'Motor':
            ...

        @property
        def controller(self) -> 'Controller':
            ...

        @property
        def observer(self) -> 'Observer':
            ...

        class Motor:
            """
            Linear dynamic model of the connected motor.
            This model can be used for estimating various internal states of the motor.
            """

            @property
            def Kt_NmPerA(self) -> float:
                """
                :return: Torque constant, in N*m/A
                """
                ...

            @property
            def Kb_VPerRadPerSec(self) -> float:
                """
                :return: Torque constant in V/(rad/sec)
                """
                ...

            @property
            def B_NmPerRadPerSec(self) -> float:
                """
                :return: Friction constant, in N*m/(rad/sec)
                """
                ...

            @property
            def Udeadzone_Volts(self) -> float:
                """
                :return: Voltage needed to make the motor moves
                """
                ...

            @property
            def R_Ohm(self) -> float:
                """
                :return: Armature resistance, in ohms
                """
                ...

            @property
            def L_Henry(self) -> float:
                """
                :return: Armature inductance, in henry
                """
                ...

            @property
            def Cp_Farad(self) -> float:
                """
                :return: Capacity of a EMI-eliminating capacitor across motor terminals, in farads
                """
                ...

            @property
            def ticksPerRevolution(self) -> float:
                """
                :return: Number of encoder ticks per one revolution.
                """
                ...

        class Controller:
            """
            Constants of the position/speed controller
            Brian implements these two controllers:
            - a parallel-form 2-degrees-of-freedom PI controller for motor speed [1], and
            - a cascaded P controller for motor position.
            [1]: https://www.mathworks.com/help/control/ug/two-degree-of-freedom-2-dof-pid-controllers.html
            """

            @property
            def speedKp(self) -> float:
                """
                :return: Proportional constant of the speed PI controller
                """
                ...

            @property
            def speedKi(self) -> float:
                """
                :return: Integral constant of the speed PI controller
                """
                ...

            @property
            def speedBeta(self) -> float:
                """
                :return: Setpoint weight in the proportional branch of the PI controller (see [1])
                """
                ...

            @property
            def positionKp(self) -> float:
                """
                :return: Proportional constant of the cascaded position P controller (its output is target speed in ticks/s)
                """
                ...

            @property
            def positionToleranceTicks(self) -> int:
                """
                :return: Tolerate up to this deviation with zero output (needed for EV3 medium motor)
                """
                ...
        class Observer:
            """
            Additional configuration of state observer.
            """

            @property
            def current(self) -> 'Current':
                """Current"""
                ...

            @property
            def speed(self) -> 'Speed':
                """Speed"""
                ...

            class Current:
                """
                Current observer parameters.
                Brian has to estimate motor winding current from H-bridge
                current measurements. These are not equal (PWM=0 makes the
                winding current impossible to directly measure).
                The way it does so is by simulating the current response
                using the provided model and then correcting the predicted
                value using real measurements (when they're available).

                """
                @property
                def measurementWeight_pct(self) -> int:
                    """
                    :return: Correction step: How much weight to give to measurements vs. model prediction
                    """
                    ...

                @property
                def minimumPwmOnTime_pct(self) -> int:
                    """
                    :return: Only trust measurements if the PWM has at least this duty cycle
                    """
                    ...

            class Speed:
                """
                Speed tracking loop parameters
                Brian estimates motor speed using a tracking loop/observer inspired by
                figure 3 and equations (6) in [2]. These constants specify the parameters
                of the loop.
                [2]: https://www.sciencedirect.com/science/article/pii/S2405896319326618
                """
                @property
                def Kp(self) -> int:
                    """"""
                    ...

                @property
                def Ki(self) -> int:
                    """"""
                    ...
