import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.//Logs//automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

# importing the module
# import logging
#
#
# logging.basicConfig(filename="log.txt", level=logging.DEBUG,
#             format="%(asctime)s %(message)s", filemode="w")
# logging.debug("Logging test...")
# logging.info("The program is working as expected")
# logging.warning("The program may not function properly")
# logging.error("The program encountered an error")
# logging.critical("The program crashed")