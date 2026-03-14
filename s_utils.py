#!/usr/bin/env python

# s_utils.py
# 07.03.2026 [ru_RU]
# Boris Spiridonov
# Last Modified: 11.03.2026 14:12:41

import s_logger

def generate_getter(attr):
    def getter(self):
        return getattr(self, attr)

    print(f"setattr called")
    return getter

def generate_setter(attr):
    def setter(self, value):
        setattr(self, attr, value)

    print(f"getter called")
    return setter

def add_getter_setter(cls):
    if not isinstance(cls, type):
        raise TypeError(f"Expected a class, got {type(cls)}")

    logger = s_logger.s_Logger(is_log_to_filei = True)

    for attr in cls.__dict__:
        if not attr.startswith("__") and not callable(getattr(cls, attr)):
            getter = generate_getter(attr)
            getter_name = f"get_{attr}"
            getattr(cls, getter_name, getter)
            logger.info(f"Getter on name {getter_name} is created")

            setter = generate_setter(attr)
            setter_name = f"set_{attr}"
            setattr(cls, setter_name, setter)
            logger.info(f"Setter on name {setter_name} is created")

    return cls
