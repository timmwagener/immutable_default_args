# -*- coding: utf-8 -*-
from array import array
from copy import deepcopy

import pytest


def test_mutable_function_with_two_default_args_remains_unaltered(
        CrossinterpreterBaseClass):

    class TestClass(CrossinterpreterBaseClass):

        def return_mutable_defaults(self, iterable_a=[], iterable_b=[]):
            return iterable_a, iterable_b

    instance = TestClass()

    for index in range(100):

        mutable_default_a, mutable_default_b = instance.return_mutable_defaults()
        assert len(mutable_default_a) == 0
        assert len(mutable_default_b) == 0

        for mutable_default in (mutable_default_a, mutable_default_b):
            mutable_default.append(index)


def test_mutable_function_default_and_pos_arg_remains_unaltered(
        CrossinterpreterBaseClass):

    class TestClass(CrossinterpreterBaseClass):

        def return_mutable_default(self, positional_arg, iterable=[]):
            return positional_arg, iterable

    instance = TestClass()

    for index in range(100):
        _, mutable_default = instance.return_mutable_default('positional_arg')
        assert len(mutable_default) == 0

        mutable_default.append(index)


def test_mutable_function_default_given_through_pos_args_is_respected(
        CrossinterpreterBaseClass):


    class TestClass(CrossinterpreterBaseClass):

        def return_mutable_default(self, positional_arg, default_arg=[]):
            return positional_arg, default_arg


    instance = TestClass()

    _, mutable_default = instance.return_mutable_default(
        'positional_arg', 'default_arg_given_as_pos_arg')

    assert isinstance(mutable_default, (str,))
    assert mutable_default == 'default_arg_given_as_pos_arg'


def test_mutable_function_default_with_classmethod(CrossinterpreterBaseClass):


    class TestClass(CrossinterpreterBaseClass):

        @classmethod
        def return_mutable_default_class(cls, positional_arg, default_arg=[]):
            return positional_arg, default_arg


    assert isinstance(TestClass.__dict__['return_mutable_default_class'],
                      (classmethod,))

    instance = TestClass()
    for index in range(100):
        _, mutable_default = instance.return_mutable_default_class('positional_arg')
        assert len(mutable_default) == 0
        _, mutable_default = TestClass.return_mutable_default_class('positional_arg')
        assert len(mutable_default) == 0

        mutable_default.append(index)


def test_mutable_function_default_with_staticmethod(CrossinterpreterBaseClass):


    class TestClass(CrossinterpreterBaseClass):

        @staticmethod
        def return_mutable_default_class(positional_arg, default_arg=[]):
            return positional_arg, default_arg

    assert isinstance(TestClass.__dict__['return_mutable_default_class'],
                      (staticmethod,))

    for index in range(100):
        _, mutable_default = TestClass.return_mutable_default_class('positional_arg')
        assert len(mutable_default) == 0

        mutable_default.append(index)