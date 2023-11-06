import logging
import logging.config

# get the logger specified in the file
logger = logging.getLogger("customLogger")
def add2Num(x,y):
    logger.info("add num function is called from module-"+ __name__)
    return int(x)+int(y)


