import logging

LOG_MODE_DEBUG = "dbg"
LOG_MODE_DEV = "dev"
LOG_MODE_PROD = "prod"


def setup_custom_logger(mode=LOG_MODE_PROD):
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    if mode == LOG_MODE_DEBUG:
        logger.setLevel(logging.DEBUG)
    elif mode == LOG_MODE_DEV:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.ERROR)
    return logger

def get_logger():
    return logging.getLogger(__name__)
