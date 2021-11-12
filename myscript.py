import sys

def say_hi(s):
    print("Hello, ", s)
    print(sys.version)
    return None

def test_say_hi():
    assert True

def test_other():
    assert False # will fail, obviously
