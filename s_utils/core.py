from time import time
from s_utils.log import g_s_log_extra, g_logger

def s_decorator(f):
    def new_func(*args, **kwargs):
        if g_s_log_extra:
            start_time = time()
            g_logger.info("Entering function {}, args: {}, kwargs: {}...".format(f.__name__, args, kwargs))
    
        if "no_log" in kwargs:
            kwargs['logger'] = None
        else:
            kwargs['logger'] = g_logger
        result = f(*args, **kwargs)
    
        if g_s_log_extra:
            end_time = time()
            g_logger.info("Exited {} ({} s)".format(f.__name__, end_time-start_time))
    
        return result
    return new_func
