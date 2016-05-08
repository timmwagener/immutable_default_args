# -*- coding: utf-8 -*-
import logging
from copy import deepcopy
from array import array

import pytest
from six import with_metaclass

from immutable_default_args import ImmutableDefaultArguments


logger = logging.getLogger(__name__)


MUTABLE_DEFAULT_VALUES = [list(), dict(), set(), bytearray(), array('i')]


class ImmutableDefaultArgumentsBase(with_metaclass(ImmutableDefaultArguments,
                                                   object)):
    pass


@pytest.fixture(params=MUTABLE_DEFAULT_VALUES)
def mutable_default_value(request):
    return deepcopy(request.param)


@pytest.fixture
def CrossinterpreterBaseClass():
    return ImmutableDefaultArgumentsBase
