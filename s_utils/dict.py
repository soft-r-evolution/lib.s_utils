import time
import logging

LOG_MODE_DEBUG = "dbg"
LOG_MODE_DEV = "dev"
LOG_MODE_PROD = "prod"

def setup_custom_logger(name = "root", mode = LOG_MODE_PROD, s_log_extra = True):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

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

try: g_logger
except NameError: g_logger = None

if not g_logger:
    g_s_log_extra = True
    g_logger = setup_custom_logger(__name__, LOG_MODE_DEBUG)

def s_decorator(f):
    def new_func(*args, **kwargs):
        if g_s_log_extra:
            start_time = time.time()
            g_logger.info("Entering function {}, args: {}, kwargs: {}...".format(f.__name__, args, kwargs))
    
        if "no_log" in kwargs:
            kwargs['logger'] = None
        else:
            kwargs['logger'] = g_logger
        result = f(*args, **kwargs)
    
        if g_s_log_extra:
            end_time = time.time()
            g_logger.info("Exited {} ({} s)".format(f.__name__, end_time-start_time))
    
        return result
    return new_func

@s_decorator
def get_key(content, key, **kwargs):
    """Check is a key value is present or not in a dictionary.
       if logger is set the value will be logged in info is present
       and warning if not present."""
    print (kwargs)
    logger = kwargs['logger']

    if not content:
        if logger:
            logger.warning("Empty dictionary detected")
        return None
    if not isinstance(content, dict):
        if logger:
            logger.warning("Invalid dictionary detected")
        return None

    if key not in content:
        if logger:
            logger.warning("key {} was not found in the dictionary".format(key))
        return None
    else:
        value = content[key]
        if logger:
            logger.info('key "{}" = "{}"'.format(key, value))
        return value
