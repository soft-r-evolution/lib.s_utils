##import time
##import logging
#
#LOG_MODE_DEBUG = "dbg"
#LOG_MODE_DEV = "dev"
#LOG_MODE_PROD = "prod"
#
#if not g_logger:
#    g_s_log_extra = True
#    g_logger = setup_custom_logger(__name__)
#
#class s_decorator(object):
#    def __init__(self, no_log = False):
#        self.no_log = no_log
#
#    def __call__(self, f):
#        if g_s_log_extra:
#            start_time = time.time()
#            g_logger.info("Entering {}, args: {}, kwargs: {}".format(f.__name__, args, kwargs))
#
#        if self.no_log:
#            kwargs['logger'] = None
#        else:
#            kwargs['logger'] = g_logger
#        result = f(*args, **kwargs)
#
#        if g_s_log_extra:
#            end_time = time.time()
#            g_logger.info("Exited {} ({} s)".format(f.__name__, end_time-start_time))
#
#        return result
#
#def setup_custom_logger(name = "root", mode = LOG_MODE_PROD, s_log_extra = True):
#    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
#
#    handler = logging.StreamHandler()
#    handler.setFormatter(formatter)
#
#    logger = logging.getLogger(name)
#    logger.addHandler(handler)
#    if mode == LOG_MODE_DEBUG:
#        logger.setLevel(logging.DEBUG)
#    elif dev == LOG_MODE_DEV:
#        logger.setLevel(logging.INFO)
#    else:
#        logger.setLevel(logging.ERROR)
#
#    return logger
#
