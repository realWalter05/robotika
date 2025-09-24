from brian.uicontrol import ButtonId


class UiEventsListener:
    """"""

    class KnobEvent:
        """"""
        turn_delta: int
        """"""
        turned_to: int
        """"""
        is_pressed: bool
        """"""
        just_pressed: bool
        """"""
        just_released: bool
        """"""

    class ButtonEvent:
        """"""
        is_pressed: bool
        """"""
        just_pressed: bool
        """"""
        just_released: bool
        """"""

    class ButtonsEvent:
        """"""
        top_left: 'UiEventsListener.ButtonEvent'
        """"""
        top_right: 'UiEventsListener.ButtonEvent'
        """"""
        bottom_left: 'UiEventsListener.ButtonEvent'
        """"""
        bottom_right: 'UiEventsListener.ButtonEvent'
        """"""
        any_button: 'UiEventsListener.ButtonEvent'
        """"""
        any_button_incl_knob: 'UiEventsListener.ButtonEvent'
        """"""

    class Button:
        last_button_event: 'UiEventsListener.ButtonEvent'  # Can be used for last button event without resetting it
        """"""

        def wait_for_press(self, timeout_ms: int = -1) -> bool:
            """
            Waits for next button press event.
            This function is blocking.

            :param timeout_ms: Maximum number of milliseconds to wait.
                - If the timeout is negative, the function will wait indefinitely.

            :return success:
                - True: If the desired button event was caught.
                - False: If the timeout ran out.
            """

        def wait_for_release(self, timeout_ms: int = -1) -> bool:
            """
            Waits for next button release event.
            This function is blocking.

            :param timeout_ms: Maximum number of milliseconds to wait.
                - If the timeout is negative, the function will wait indefinitely.

            :return success:
                - True: If the desired button event was caught.
                - False: If the timeout ran out.
            """

        def wait_for_press_and_release(self, timeout_ms: int = -1) -> bool:
            """
            Waits for next button press and release event.
            This function is blocking.

            :param timeout_ms: Maximum number of milliseconds to wait.
                - If the timeout is negative, the function will wait indefinitely.

            :return success:
                - True: If the desired button event was caught.
                - False: If the timeout ran out.
            """

    class Knob(Button):
        last_button_event: 'UiEventsListener.KnobEvent'  # Can be used for last knob event without resetting it
        """"""

        def wait_for_directional_turn(self, clockwise: bool, timeout_ms: int = -1) -> bool:
            """
            Waits for next directional turn of the knob.
            This function is blocking.

            :param clockwise: Whether to wait for clockwise or counterclockwise turn.
            :param timeout_ms: Maximum number of milliseconds to wait.
                - If the timeout is negative, the function will wait indefinitely.

            :return success:
                - True: If the desired button event was caught.
                - False: If the timeout ran out.
            """

        def wait_for_any_turn(self, timeout_ms: int = -1) -> bool:
            """
            Waits for next any turn of the knob.
            This function is blocking.

            :param timeout_ms: Maximum number of milliseconds to wait.
                - If the timeout is negative, the function will wait indefinitely.

            :return success:
                - True: If the desired button event was caught.
                - False: If the timeout ran out.
            """

    top_left_button: Button
    """"""
    top_right_button: Button
    """"""
    bottom_left_button: Button
    """"""
    bottom_right_button: Button
    """"""
    any_button: Button
    """"""
    any_button_incl_knob: Button
    """"""
    knob: Knob
    """"""

    def __init__(self):
        """
        Initializes a new UiEventsListener class.
        """
        ...

    def knob_event_since_last(self) -> KnobEvent:
        """
        This function will reset just_pressed, just_released fields and turn_delta fields.

        :return: KnobEvent class of events that happened since last call.
        """
        ...

    def buttons_event_since_last(self) -> ButtonsEvent:
        """
        This function will reset just_pressed and just_released fields.

        :return: ButtonsEvent class of events that happened since last call.
        """
        ...
