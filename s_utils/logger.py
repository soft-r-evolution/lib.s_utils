import logging


def get_logger():
    """ Return a s_utils logger """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    return logger
