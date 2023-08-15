# Importing from the module 'hello' the function 'hello'
from hello import hello

def test_default():
    assert hello() == "hello, world!"


def test_argument():
    assert hello("R") == "hello, R"