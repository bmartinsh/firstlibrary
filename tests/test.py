# tests/test_lib.py
from firstlibrary.lib import try_me

def test_try_me():
    assert len(try_me()) != 0
