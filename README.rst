Immutable defaults arguments
============================

This module provides facilities for turning mutable default function arguments
into immutable ones. It is fairly lightweight and has no non-standard dependencies.
You can install this package with the standard ``pip`` command::

    $ pip install immutable_default_args

The issue with `mutable argument default values <http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument>`_ is pretty well known in Python.
Basically mutable default values are assigned once at define time and can then
be modified within the function body which might come as a surprise.
Here is the example from the `stackoverfow <http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument>`_ thread::

    def foo(a=[]):
        a.append(5)
        return a

    >>> foo()
    [5]
    >>> foo()
    [5, 5]
    >>> foo()
    [5, 5, 5]
    ...

The default way of preventing this behaviour is to use ``None`` as the default
and check for it in the function body, like so::

    def foo(a=None):
        a = a if (type(a) is list) else []
        a.append(5)
        return a

    >>> foo()
    [5]
    >>> foo()
    [5]
    ...

Usage
-----

This package aims to offer two additional options to fix this issue:

* With a handy function decorator ``@fix_mutable_kwargs`` to fix a certain function.
* With a metaclass ``ImmutableDefaultArguments`` to fix all *methods*, *classmethods* and *staticmethods* at once.

Using the decorator::

    from immutable_default_args import fix_mutable_kwargs

    @fix_mutable_kwargs
    def foo(a=[]):
        a.append(5)
        return a

    >>> foo()
    [5]
    >>> foo()
    [5]
    ...

It doesn't matter if the iterable is empty or not::

    @fix_mutable_kwargs
    def foo(a=[1, 2, {'key': 'value'}, 3, 4]):
        a.append(5)
        return a

    >>> foo()
    [1, 2, {'key': 'value'}, 3, 4, 5]
    >>> foo()
    [1, 2, {'key': 'value'}, 3, 4, 5]
    ...

Fixing all mutable default values for all methods of an object via the
``ImmutableDefaultArguments`` metaclass::

    class Foo(object):

        __metaclass__ = ImmutableDefaultArguments  # Py2 syntax

        def foo(self, a=[]):
            a.append(5)
            return a

        @classmethod  # staticmethods work as well
        def foo_classmethod(cls, a=[]):
            a.append(5)
            return a

    instance_of_foo = Foo()
    >>> instance_of_foo.foo()
    [5]
    >>> instance_of_foo.foo()
    [5]
    ...
    >>> Foo.foo_classmethod()
    [5]
    >>> Foo.foo_classmethod()
    [5]

Compatibility
-------------

The ``immutable_default_args`` package is tested against Py2/3 and is supported
from *Py2.7* upstream.

Changelog
---------

0.0.5 *(08.05.2016)*
********************
* Fixed documentation

0.0.2 *(08.05.2016)*
********************
* Added ``@fix_mutable_kwargs`` decorator
* Refactorings/Cleanup

0.0.1 *(08.05.2016)*
********************
* First release. Included only ``ImmutableDefaultArguments`` metaclass

License
-------

You are free to do whatever you like with the code. Please note that I am not
accountable for anything that might have happened as a result of executing the
code from the ``immutable_default_args`` package....ever.