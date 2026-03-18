import logging

def module_a_func():
    logger = logging.getLogger('')
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')