import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsermail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getExpected_login_title():
        expected_login_title = config.get('common info', 'expected_login_title')
        return expected_login_title

    @staticmethod
    def getExpected_title():
        expected_title = config.get('common info', 'expected_title')
        return expected_title