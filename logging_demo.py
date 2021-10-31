#!/usr/bin/env/python

""" logging_demo.py : Script to demonstrate logging module of python """

__author__ = "John Doe"
__credits__ = ["John Doe"]
__version__ = "1.0.0"
__maintainer__ = "John Doe"
__email__ = "JohnDoe@gmail.com"
__status__ = "Prototype"

import os
import sys
import logging
from datetime import datetime

JOB_NAME = 'JobName'
LOG_DIR_NAME = 'logs'
LOGGING_LOG_FORMAT = "%(asctime)s [ %(levelname)s ] : %(message)s"
LOGGING_DATE_FORMAT = "%Y%m%d %H:%M:%S"

LOGGING_LEVEL = logging.DEBUG
LOGGER = None

def generate_log_file_name():
    """ Method to generate new log file name with timestamp """
    return "".join( [ 
        JOB_NAME,
        '_',
        datetime.now().strftime('%Y%m%d%H%M%S'),
        '.log'
    ] )

def init_logging():
    """ Method to initialize logging configurations """

    global LOGGER

    LOGGER = logging.getLogger( "Logger" )
    LOGGER.setLevel( LOGGING_LEVEL )

    formatter = logging.Formatter( LOGGING_LOG_FORMAT, LOGGING_DATE_FORMAT )

    fileHandler = logging.FileHandler( os.path.join( LOG_DIR_NAME, generate_log_file_name() ) )
    fileHandler.setLevel( LOGGING_LEVEL )
    fileHandler.setFormatter( formatter )

    streamHandler = logging.StreamHandler()
    streamHandler.setLevel( LOGGING_LEVEL )
    streamHandler.setFormatter( formatter )

    LOGGER.addHandler( fileHandler )
    LOGGER.addHandler( streamHandler )

def init_directories():
    """ Method to initialize work directories if not exists """
    if not os.path.exists( LOG_DIR_NAME ):
        os.mkdir( LOG_DIR_NAME )

def initialize():
    """ Initializer method : To initialize objects """
    init_directories()
    init_logging()
    LOGGER.info( f"Initialization finished for Job : {JOB_NAME}" )

if __name__ == "__main__":

    initialize()
    
    LOGGER.info( f"This information will be printed in logs!!!" )
    LOGGER.debug( f"Logging is running in DEBUG mode." )
    LOGGER.warning( f"This is a warning" )
    LOGGER.error( f"Error encountered!" )
