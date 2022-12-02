import logging

class LogGenerate():
    @staticmethod
    def loggen():
        logging.basicConfig(filename='C://Users//befor//PycharmProjects//OpenCartV1_Selenium_Python//'
                                     'automation.log',format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger