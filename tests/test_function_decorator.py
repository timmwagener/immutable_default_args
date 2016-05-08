# -*- coding: utf-8 -*-


import immutable_default_args


def test_function_is_not_altered_since_it_has_no_args(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    @immutable_default_args.fix_mutable_kwargs
    def test_function():
        return None

    assert not mutable_to_immutable_kwargs_mock.called


def test_function_is_not_altered_since_it_has_only_pos_args(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    @immutable_default_args.fix_mutable_kwargs
    def test_function(argument_a, argument_b):
        return None

    assert not mutable_to_immutable_kwargs_mock.called


def test_function_is_not_altered_since_it_has_only_star_args(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    @immutable_default_args.fix_mutable_kwargs
    def test_function(*args, **kwargs):
        return None

    assert not mutable_to_immutable_kwargs_mock.called


def test_classmethod_is_not_altered(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    class TestClass(object):

        @immutable_default_args.fix_mutable_kwargs
        @classmethod
        def test_function(cls, argument_a, test=5, *args, **kwargs):
            return None

    assert not mutable_to_immutable_kwargs_mock.called


def test_staticmethod_is_not_altered(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    class TestClass(object):

        @immutable_default_args.fix_mutable_kwargs
        @staticmethod
        def test_function(argument_a, test='immutable', *args, **kwargs):
            return None

    assert not mutable_to_immutable_kwargs_mock.called


def test_function_is_altered_when_one_kwarg(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    @immutable_default_args.fix_mutable_kwargs
    def test_function(test=[], *args, **kwargs):
        return None

    names_to_defaults = {'test': []}
    pos_arg_names = []
    mutable_to_immutable_kwargs_mock.assert_called_with(names_to_defaults,
                                                        pos_arg_names)


def test_classmethod_is_altered(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    class TestClass(object):

        @immutable_default_args.fix_mutable_kwargs
        @classmethod
        def test_function(cls, argument_a, test={'key':'value'}, *args, **kwargs):
            return None

    names_to_defaults = {'test':{'key':'value'}}
    pos_arg_names = ['cls', 'argument_a']
    mutable_to_immutable_kwargs_mock.assert_called_with(names_to_defaults,
                                                        pos_arg_names)


def test_staticmethod_is_altered(mocker):

    mutable_to_immutable_kwargs_mock = mocker.patch.object(
        immutable_default_args, 'mutable_to_immutable_kwargs')

    class TestClass(object):

        @immutable_default_args.fix_mutable_kwargs
        @staticmethod
        def test_function(argument_a, test=[0,1,2,3], *args, **kwargs):
            return None

    names_to_defaults = {'test': [0,1,2,3]}
    pos_arg_names = ['argument_a']
    mutable_to_immutable_kwargs_mock.assert_called_with(names_to_defaults,
                                                        pos_arg_names)