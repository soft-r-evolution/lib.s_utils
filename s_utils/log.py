import logging

LOG_MODE_DEBUG = "dbg"
LOG_MODE_DEV = "dev"
LOG_MODE_PROD = "prod"


def setup_custom_logger(name="root", mode=LOG_MODE_PROD, s_log_extra=True):
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    if mode == LOG_MODE_DEBUG:
        logger.setLevel(logging.DEBUG)
    elif mode == LOG_MODE_DEV:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.ERROR)

    return logger


try:
    g_logger
except NameError:
    g_logger = None

if not g_logger:
    g_s_log_extra = True
    g_logger = setup_custom_logger(__name__, LOG_MODE_DEBUG)
