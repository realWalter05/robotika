from typing import List, Union
from enum import Enum
from UiEventsListener import *


class UiEventsListenerAlreadyClosedError(Exception):
    """Thrown when trying to access closed UiEventsListener"""


class LedColor:
    def __init__(self, red: int, green: int, blue: int):
        """
        Holds color definition for UI LEDs. Color values range from 0 to 255. When outside of this range, the values are clamped
        """
        ...

    red: int
    """Red component of the color, in range from 0 to 255. When set to a value outside of this range, the value is clamped"""
    green: int
    """Green component of the color, in range from 0 to 255. When set to a value outside of this range, the value is clamped"""
    blue: int
    """Blue component of the color, in range from 0 to 255. When set to a value outside of this range, the value is clamped"""


class ButtonId(Enum):
    """"""
    TOP_LEFT = 0
    """"""
    TOP_RIGHT = 1
    """"""
    BOTTOM_LEFT = 2
    """"""
    BOTTOM_RIGHT = 3
    """"""
    KNOB = 4
    """"""


class LedButtonAnimation(Enum):
    """Constants for selecting behavior of button LEDs. Only in use when LED animations are handled by Brian OS."""

    OFF = 0
    """LED is fully off"""

    STANDBY = 1
    """LED is pulsing at low brightness level"""

    SELECTABLE = 2
    """LED is pulsing at medium brightness level"""

    SELECTED = 3
    """LED is pulsing at high brightness level"""

    inherit = 4
    """LED behavior is not set at this level; Behavior of a previous (system) level is used."""


@staticmethod
def set_button_led(target: Union[ButtonId, UiEventsListener.Button, UiEventsListener.Knob],
                   animation: LedButtonAnimation,
                   color: LedColor = 'DEFAULT_COLOR_FROM_SETTINGS') -> None:
    """
    Set desired animation and color for a specific button (target). These settings override the animation requested
    by the `PhysButtonOverlay` and the default os button effect, unless `LedButtonAnimation.inherit` is used.

    :param target: Target button to change color. When Using UiEventsListener.any_button and
    UiEventsListener.any_button_incl_knob, all respective buttons change color/animation.
    :param animation: Target animation.
    :param color: Target color. When unfilled default color from settings is used.
    """
    ...


@staticmethod
def enable_knob_rotation_animation(enabled: bool) -> None:
    """
    If enabled, OS automatically animates the LEDs under the knob when it rotates. The user program starts in the enabled state.

    :param enabled: Whether to animate knob rotation.
    """
    ...


# @staticmethod
# def get_num_of_leds() -> int:
#     """
#     :return: number of available leds
#     """
#     ...
