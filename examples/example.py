import logging
from time import sleep
from milestone_timer import MilestoneTimer

log_format_string = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(
    level="DEBUG",
    format=log_format_string,
)

logger = logging.getLogger(__name__)

mt = MilestoneTimer("Let's play!")

# Code here to meet the contestants
sleep(0.1)

logger.debug(mt.add_milestone("Met the contestants"))

# Code here to rotate the board
sleep(0.2)

logger.debug(mt.add_milestone("Rotated board"))

# Code here for numberwang
sleep(0.05)

logger.debug(mt.add_milestone("That's numberwang"))

print(mt)
