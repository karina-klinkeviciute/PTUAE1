import logging

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s, %(name)s, %(levelname)s, %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info("info message")

