from enum import Enum, auto
from threading import Timer
from threading import Thread
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("turn")


class Phase(Enum):
    TURN_INIT = 0
    FAST_ACT = auto()
    MOVEMENT = auto()
    MAIN_ACT = auto()
    INPUT = auto()
    IMMEDIATELY_ACT = auto()
    TURN_END = auto()


# class PhaseTimer(Timer):


# def print_hello():
#      print("hello world")

# class RepeatingTimer(Timer):
#     def run(self):
#         self.finished.wait(self.interval)
#         while not self.finished.is_set():
#             self.function(*self.args, **self.kwargs)
#             self.finished.wait(self.interval)


class Turn(Thread):
    """Class for managing a turn"""

    schedules = {
        Phase.TURN_INIT: [],
        Phase.FAST_ACT: [],
        Phase.MOVEMENT: [],
        Phase.MAIN_ACT: [],
        Phase.INPUT: [],
        Phase.IMMEDIATELY_ACT: [],
        Phase.TURN_END: [],
    }
    phase = Phase.INPUT
    # phase_timer = Timer()

    def transition(self):
        self.phase = Phase((self.phase.value + 1) % Phase.__len__())
        logger.info("Transfer to '%s'", self.phase)

    def register(self, phase, action):
        if self.phase != Phase.INPUT:
            logger.warning("Shouldn't register actions out of 'INPUT' phase")
            return
        self.schedules[phase].append(action)
        logger.info("'%s' has been added to '%s'", action.__name__, phase)



def fff():
    return


tt = Turn()
tt.register(Phase.IMMEDIATELY_ACT, fff)


tt.transition()
tt.transition()
tt.transition()
tt.transition()
tt.transition()
tt.transition()
tt.transition()
tt.transition()
tt.transition()
tt.transition()




# Unittest
class TurnUnitTest(unittest.TestCase):
    def test_transition(self):
        tt = Turn()
        with self.assertLogs("turn", level="DEBUG") as cm:
            tt.transition()
            tt.transition()
            tt.transition()
            tt.transition()
            tt.transition()
            tt.transition()
            tt.transition()
            tt.transition()
            tt.transition()
            tt.transition()
        self.assertEqual(
            cm.output,
            [
                "INFO:turn:Transfer to 'Phase.FAST_ACT'",
                "INFO:turn:Transfer to 'Phase.MOVEMENT'",
                "INFO:turn:Transfer to 'Phase.MAIN_ACT'",
                "INFO:turn:Transfer to 'Phase.INPUT'",
                "INFO:turn:Transfer to 'Phase.IMMEDIATELY_ACT'",
                "INFO:turn:Transfer to 'Phase.TURN_END'",
                "INFO:turn:Transfer to 'Phase.TURN_INIT'",
                "INFO:turn:Transfer to 'Phase.FAST_ACT'",
                "INFO:turn:Transfer to 'Phase.MOVEMENT'",
                "INFO:turn:Transfer to 'Phase.MAIN_ACT'",
            ],
        )

# unittest.main()
