import logging, logging.config
# from oop_from_material import Animal, DogCat

from datetime import datetime

from random import randint
# import oop_from_material

now = datetime.now()

random_number = randint(1, 12)

print(random_number)

# from oop_from_material import *

# animal = Animal("rabbit")

# dogcat = DogCat("Fluffy", "mixed", "white")



# import python_advanced_logging, python_advanced_logging.config

# set up logging
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("sLogger")

# log something
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")


try:
    with open("lesson3-tuple.py", 'rb') as f:
        ...
    logger.info('File successfully read')
except Exception as e:
    logger.error('Failed to open: ' + str(e))
