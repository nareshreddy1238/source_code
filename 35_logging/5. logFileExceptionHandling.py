import logging

try:
    print(sal)
except Exception as exp:
    logging.basicConfig(
        level=logging.ERROR,
        filename='5. logFileExceptionHandling.log',
        filemode='w',
        format= '%(asctime)s - %(message)s - %(name)s - %(levelname)s'
    )
    logging.error('Error Occurred:', exc_info=True)

