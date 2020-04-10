from s_utils.dict import get_key

import pytest

def test_get_key():
    assert get_key(None, None) == None
