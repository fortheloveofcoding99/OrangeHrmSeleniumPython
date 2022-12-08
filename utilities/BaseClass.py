import logging

class BaseClass:
    def getLogger(self):
         logger = logging.getLogger(__name__)
         fileHandlr=logging.FileHandler('logfile.log') # where all the logfile will be saved
         formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s') #format to print
         fileHandlr.setFormatter(formatter)
         logger.addHandler(fileHandlr)
         logger.setLevel(logging.INFO) # setting the level of logging
         return logger