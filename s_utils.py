#!/usr/bin/env python

# s_utils.py
# 07.03.2026 [ru_RU]
# Boris Spiridonov
# Last Modified: 07.03.2026 14:42:19

def generate_getter(attr):
    def getter(self):
        return getattr(self, attr)
    return getter

def generate_setter(attr):
    def setter(self, value):
        setattr(self, attr, value)
    return

def add_getter_setter(cls, name, bases):
    for attr in cls.__dict__:
        if not attr.startswith("__") and not callable(getattr(cls, attr)):
            getter = generate_getter(attr)
            getter_name = f"get_{attr}"
            setattr(cls, getter_name, getter)

            setter = generate_setter(attr)
            setter_name = f"set_{attr}"
            setattr(cls, setter_name, setter)

    return cls
