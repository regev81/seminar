import logging
import os
import time
from Constants import LOG_DIR
'''
file to create and configure logger
'''

log_name = time.strftime("%Y%m%d-%H%M%S.log")
log_path = os.path.join(LOG_DIR, log_name)
log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = log_path,
                    level=logging.INFO,
                    format=log_format,
                    filemode = 'w')
logger = logging.getLogger()


# wrapper function to print functions calls to log
def log_func(func):
    def wrap(*args, **kwargs):
        logger.info(f"{func.__name__}()")
        result = func(*args, **kwargs)
        return result
    return wrap