import logging

## Configure the basic logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a+b
    logger.debug(f"Adding : {a} + {b} = {result}")
    return result

def substract(a, b):
    result = a-b
    logger.debug(f"Substracting : {a} - {b}= {result}")
    return result

def multipy(a, b):
    result = a*b
    logger.debug(f"Multiplying : {a} * {b}= {result}")
    return result

def divide(a, b):
    try:
        result = a/b
        logger.debug(f"Dividing : {a} * {b}= {result}")
        return result
    except Exception as e:
        logger.error(f"Error : {e}")
        return None
    
add(10, 15)
substract(15, 10)
multipy(10, 20)
divide(20, 0)