import logging

# create a custom logger
#logger = logging.getLogger(__name__)
logger = logging.getLogger("Custom Logger")
#print(logger)
#print(__name__)

# create handlers and set the level
f_handler = logging.FileHandler('6. custom_logger.log', mode='w')
f_handler.setLevel(logging.ERROR)

# create formatters and add it to handler
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add the handler to the logger
logger.addHandler(f_handler)

# Log the output
logger.error("This is an Error")