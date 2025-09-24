def play_tone(tone: int, duration_ms: int):
    """
    Play a sine tone to the audio output.
    This method returns instantly and the tone is played in the background.

    :param tone: Frequency in Hz to play.
    :param duration_ms: How long should the tone last

    """
    ...


def stop_tone():
    """
    If tone is playing because of previous call to `play_tone`, it is stopped early.
    """
    ...
