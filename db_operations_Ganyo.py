
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

#Logging Configuration for the project
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')






def main():
    logging.info("Program started")
    # Your main code goes here
    logging.info("Program ended")

if __name__ == "__main__":
    main()




