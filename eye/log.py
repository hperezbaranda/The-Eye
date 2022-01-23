import logging


def getLog(manager):
    # Creating custom logger
    logger = logging.getLogger(manager)

    # Setting the log level
    logger.setLevel(logging.DEBUG)

    # Creating formatter
    # formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    format = logging.Formatter("%(asctime)s || %(levelname)s || %(message)s")
    # logging.basicConfig(format=format)

    # Creating Handler
    file_handler = logging.FileHandler("eye.log")

    # #Adding Formatter to Handler
    file_handler.setFormatter(format)

    
    #Adding Handlers to logger
    logger.addHandler(file_handler)

    return logger
