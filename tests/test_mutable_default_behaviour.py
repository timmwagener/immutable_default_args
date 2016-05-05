# -*- coding: utf-8 -*-
from array import array

import pytest


@pytest.fixture
def SimpleClass(CrossinterpreterBaseClass):
    class SimpleClass(CrossinterpreterBaseClass):
        pass
    return SimpleClass


def test_interpreter_dependent_instanciation(CrossinterpreterBaseClass,
                                             SimpleClass):
    """Instanciation of a class with Py2/3 compliant metaclass works properly.
    """
    test_class_instance = SimpleClass()
    assert isinstance(test_class_instance, SimpleClass)
    assert type(type(test_class_instance)) is type(SimpleClass) is type(CrossinterpreterBaseClass)


@pytest.fixture
def ClassWithMutableFuncDefaultNoFix(mutable_default_value):

    class ClassWithMutableFuncDefaultNoFix(object):

        def return_mutable_default(self, iterable=mutable_default_value):
            return iterable

    return ClassWithMutableFuncDefaultNoFix


def test_mutable_function_default_is_altered(ClassWithMutableFuncDefaultNoFix):
    """Here we assert the default behaviour, that the mutable is altered,
    which often is perceived as surprising.
    """
    instance = ClassWithMutableFuncDefaultNoFix()

    ids = set()
    for index in range(100):

        mutable_default = instance.return_mutable_default()
        ids.add(id(mutable_default))

        assert len(mutable_default) == index

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

        assert len(mutable_default) == index + 1  # values have been added to same obj.
        assert len(ids) == 1  # same memory address
