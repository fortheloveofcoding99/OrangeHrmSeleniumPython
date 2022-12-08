import inspect
import logging

class BaseClass:
    def getLogger(self):
         loggerName = inspect.stack()[1][3]
         logger = logging.getLogger(loggerName)
         fileHandlr=logging.FileHandler('logfile.log') # where all the logfile will be saved
         formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s') #format to print
         fileHandlr.setFormatter(formatter)
         logger.addHandler(fileHandlr)
         logger.setLevel(logging.INFO) # setting the level of logging
         return logger