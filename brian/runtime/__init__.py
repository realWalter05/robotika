def enable_turn_off_by_buttons(enabled: bool) -> None:
    """
    If enabled (default), first press of any left together with any right button will send a KeyboardInterrupt.
    The second such press will hard abort the program.
    If disabled, the buttons will not be watched and the program can use them fully according to the
    programmer's needs. It is the programmer's responsibility to provide alternative shutdown mechanism.
    If no such mechanism is provided, the only two ways to exit a stuck program is to
    either eject the sd card or force power off of the entire brick.
    :param enabled: true if the Brian should watch for the turn-off button pattern, false to ignore it.
    """
    ...


def power_off() -> None:
    """
    Shutdowns Brian.

    When Brian shutdown is requested, but it is still connected to power via USB, only a partial shutdown is performed.
    All peripheral functions (ports, audio, display, ...) are shut down,
    but internal functions, such as battery charging and monitoring are still running.
    """
    ...


def reboot_brian() -> None:
    """
    Reboots Brian.

    This will put Brian back to the main menu screen.
    """
    ...


#
# Preview features:
#
# def battery_level() -> int:
#     """
#     :return: Battery level in percents.
#     """
#     ...
#
#
# def battery_voltage() -> float:
#     """
#     :return: Current battery voltage in V.
#     """
#     ...
#
#
# def is_plugged_in() -> bool:
#     """
#     :return: whether brian is plugged in or not.
#     """
#     ...
#
#
# def is_plugged_in_fast_charger() -> bool:
#     """
#     :return: whether brian is plugged into a fast charger.
#     """
#     ...
#
#

