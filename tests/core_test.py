from s_utils.dict import get_key


def test_no_log():
    assert not get_key(None, None, no_log=1)
    assert not get_key(None, None, no_log=True)
    # should test log is empty


def test_log():
    assert not get_key(None, None)
    assert not get_key(None, None, no_log=0)
    assert not get_key(None, None, no_log=False)
    # should test log is not empty
