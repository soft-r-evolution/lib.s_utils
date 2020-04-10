from s_utils.dict import get_key


def test_get_key():
    assert not get_key(None, None)
