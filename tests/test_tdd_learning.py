#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tdd_learning
----------------------------------

Tests for `tdd_learning` module.
"""

import pytest
from tdd_learning.calc import Calc


def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)

    assert res == 9


def test_add_three_numbers():
    c = Calc()

    res = c.add(4, 5, 6)

    assert res == 15
