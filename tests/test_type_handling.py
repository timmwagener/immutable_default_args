# -*- coding: utf-8 -*-
from array import array

import pytest


@pytest.fixture
def ClassWithMutableFuncDefault(CrossinterpreterBaseClass, mutable_default_value):

    class ClassWithMutableFuncDefault(CrossinterpreterBaseClass):

        def return_mutable_default(self, iterable=mutable_default_value):
            return iterable

    return ClassWithMutableFuncDefault


def test_mutable_function_default_remains_unaltered(ClassWithMutableFuncDefault):

    instance = ClassWithMutableFuncDefault()

    for index in range(100):

        mutable_default = instance.return_mutable_default()
        assert len(mutable_default) == 0

        if (isinstance(mutable_default, (list, bytearray, array))):
            mutable_default.append(index)  # append something
        elif (isinstance(mutable_default, (dict, ))):
            mutable_default.setdefault(index, 'value')
        elif (isinstance(mutable_default, (set, ))):
            mutable_default.add(index)
        else:
            msg = "Unknown mutable type {0}"
            msg = msg.format(type(mutable_default).__name__)
            raise TypeError(msg)
