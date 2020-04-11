from time import time
from s_utils.log import *

try:
    logger
except NameError:
    logger = setup_custom_logger(LOG_MODE_DEBUG)

def is_no_log(**kwargs):
    """ Return true is no_log value = True or 1 """
    if "no_log" in kwargs:
        no_log = kwargs["no_log"]
        if no_log or no_log == 1:
            return True
    return False

def s_decorator(f):
    def new_func(*args, **kwargs):
        logger = get_logger()
        no_log = is_no_log(**kwargs)
        if not no_log:
            start_time = time()
            logger.debug(
                "Entering function {}, args: {}, kwargs: {}...".format(
                    f.__name__, args, kwargs
                )
            )

        if no_log:
            kwargs["logger"] = None
        else:
            kwargs["logger"] = logger
        result = f(*args, **kwargs)

        if not no_log:
            end_time = time()
            logger.debug("Exited {} ({} s)".format(f.__name__, end_time - start_time))

        return result

    return new_func
