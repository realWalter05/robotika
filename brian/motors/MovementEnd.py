from enum import Enum
class MovementEnd(Enum):
    """
    Reasons for movement end.
    """

    FINISHED = 0
    """Movement finished"""
    TIMED_OUT = 1
    """Timed out"""
