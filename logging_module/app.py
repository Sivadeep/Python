import logging
logging.basicConfig(level=logging.DEBUG,  
	format="%(asctime)s->%(levelname)s->%(message)s")
logging.info("Info message")
logging.debug("Debug message.")
logging.warn("Warning message")
logging.error("Error mesasage")
logging.exception("exception message.")