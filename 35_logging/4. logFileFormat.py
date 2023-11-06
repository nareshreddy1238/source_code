import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='4. logFileFormat.log',
    filemode='w',
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.debug('This is a debug message')
logging.info('This is a info message')

