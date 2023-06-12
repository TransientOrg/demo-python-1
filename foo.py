import logging
import os

nums = [i for i in range(10)]

a = 1
b = 2
assert a == 1
breakpoint()
breakpoint()
print(b, nums)


def baz(a=None):
    if a is None:
        a = []
    return 0


def aaa(a=None):
    if a is None:
        a = []
    return 1


def foo(b=None):
    if b is None:
        b = []
    return 1


def bar(a):
    return 1


import os

filename = os.tmpnam()
with open(filename, "w") as f:
    pass


def boom(a=None):
    if a is None:
        a = []
    breakpoint()
    filename = os.tmpnam()
    breakpoint()
    return filename


def another_test_method():
    f = open("/tmp/.deepsource.toml", "r")
    f.write("config file.")
    f.close()
    print("abc")


filename = os.tmpnam()
