from s_utils.dict import get_key

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def test_get_key():
    assert not get_key(None, None)
    assert not get_key(2, None)
    assert not get_key(2, "value")
    test_dict = dict()
    test_dict["a"] = 12
    test_dict["b"] = 2
    assert not get_key(test_dict, "c")
    assert get_key(test_dict, "a") == 12


def test_get_key_logger():
    assert not get_key(None, None, logger)
    assert not get_key(2, None, logger)
    assert not get_key(2, "value", logger)
    test_dict = dict()
    test_dict["a"] = 12
    test_dict["b"] = 2
    assert not get_key(test_dict, "c", logger)
    assert get_key(test_dict, "a", logger) == 12
