import logging


def log_error():
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %("
                                                                        "message)s", filemode='a')

    # Creating an object
    logger = logging.getLogger()

    return logger

