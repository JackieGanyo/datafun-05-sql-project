
'''
Operations Script
This script contains functions for performing database operations in the datafun-05-sql-project.
It requires the following imports:
import sqlite3
import pandas as pd
import datetime

'''
# Import Standard Libraries
import os
import sys
import sqlite3

#Import External Libraries
import pandas as pd
import pyarrow as pa
import datetime
'''Logging Configuration for the project
logging.basicConfig(
    filename='log.txt',
    level=logging.DEBUG, 
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
    )
 # Example usage:
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
'''