import configparser # to read the data from the config files
import os

config = configparser.RawConfigParser()
config.read(os.getcwd()+'\configurations\config.ini')

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url=config.get('commonInfo','baseUrl') # name inside the config.ini file 'commoon info' and ke baseUrl
        return url

    @staticmethod
    def getUsername():
        username=config.get('commonInfo','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('commonInfo','password')
        return password