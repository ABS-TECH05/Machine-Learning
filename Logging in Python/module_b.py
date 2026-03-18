import logging

def module_b_func():
    logger = logging.getLogger('')
    logger.error('This is an error message')
    logger.critical('This is a critical message')