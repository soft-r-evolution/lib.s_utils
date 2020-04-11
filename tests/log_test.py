from s_utils.dict import get_key
from s_utils.log import *


def test_dev_mode():
    setup_custom_logger(LOG_MODE_DEV)

    assert not get_key(None, None)
    #should test log contain all message

def test_debug_mode():
    setup_custom_logger(LOG_MODE_DEBUG)

    assert not get_key(None, None)
    #should test log doesn't contain debug messages

def test_prod_mode():
    setup_custom_logger()

    assert not get_key(None, None)
    #should test log contain only error messages
