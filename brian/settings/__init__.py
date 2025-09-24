def set_volume(percent: float) -> None:
    """
    Set current volume
    :param percent: Percentage of the maximum volume to apply. The value will be clipped to range 0% ~ 100%.
    The volume will not be set higher, than the one set in the settings in main menu.
    """


def get_current_volume() -> float:
    """
    :return: Current speaker volume in percent (0% ~ 100%).
    """


def get_preferred_volume() -> float:
    """
    :return: Speaker volume that was set in the settings in main menu (0% ~ 100%).
    """


def set_lcd_brightness(percent: float) -> None:
    """
    Set current lcd brightness
    :param percent: Percentage of the maximum brightness to apply. The value will be clipped to range 1% ~ 100%.
    The brightness will not be set higher, than the one set in the settings in main menu.
    """


def get_current_lcd_brightness() -> float:
    """
    :return: Current lcd brightness in percent (1% ~ 100%).
    """


def get_preferred_lcd_brightness() -> float:
    """
    :return: Lcd brightness value that was set in the settings in main menu (0% ~ 100%).
    """


def enable_os_button_sounds(enable: bool) -> None:
    """
    :param enable: Whether to enable or disable os click sounds.
    Works only if OS is not muted in the settings in main menu.
    """


def are_os_button_sounds_enabled() -> bool:
    """
    :return: Whether os clicks are enabled (not muted).
    """


def are_os_button_sounds_preferred() -> bool:
    """
    :return: Whether os clicks were enabled in the settings in main menu.
    """
