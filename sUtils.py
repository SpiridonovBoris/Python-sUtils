#!/usr/bin/env python

# sUtils.py
# 07.03.2026 [ru_RU]
# Boris Spiridonov
# Last Modified: 01.06.2026 00:50:22

import inspect

def generate_getter(attr):
    def getter(self):
        return getattr(self, attr)

    return getter

def generate_setter(attr):
    def setter(self, value):
        setattr(self, attr, value)

    return setter

def generate_bool_checker(attr):
    def bool_checker(self):
        return getattr(self, attr)

    return bool_checker

def clean_bool_prefix(attr_name):
    attr_name = (attr_name[3:] if attr_name.startswith('is_') else attr_name)
    attr_name = (attr_name[4:] if attr_name.startswith('has_') else attr_name)

    return attr_name

def add_getter_setter(cls):
    if not isinstance(cls, type):
        raise TypeError(f"Expected a class, got {type(cls)}")

    sig = inspect.signature(cls.__init__)
    init_params = []
    for param_name in sig.parameters.keys():
        if param_name != 'self':
            init_params.append(param_name)

    for attr in init_params:
        param = sig.parameters[attr]
        param_type = param.annotation

        if param_type == bool:
            clean_name = clean_bool_prefix(attr)
            bool_checker = generate_bool_checker(attr)
            bool_checker_name = f"is_{clean_name}"
            setattr(cls, bool_checker_name, bool_checker)

        else:
            getter = generate_getter(attr)
            getter_name = f"get_{attr}"
            setattr(cls, getter_name, getter)

        setter = generate_setter(attr)
        setter_name = f"set_{attr}"
        setattr(cls, setter_name, setter)

    return cls
