import logging
"""
DEBUG 10
INFO  20
WARNING 30
ERROR 40
CRITICAL 50
"""
LOG_FORMAT='%(levelname)s %(asctime)s  - %(message)s'
logging.basicConfig(filename='output.log',level=logging.DEBUG,format=LOG_FORMAT,filemode='w')
logger=logging.getLogger()
logger.info("This is an informations!")
logger.debug("Debug Messages")
logger.warning("Warning Messages")
logger.error("An Error!")
logger.critical("Critical Issue!")