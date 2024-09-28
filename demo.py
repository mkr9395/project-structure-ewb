# from src.logger import logging
from logger import logging
from src.exceptions import USvisaException
import sys

logging.info("Welcome to our custom log")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)


