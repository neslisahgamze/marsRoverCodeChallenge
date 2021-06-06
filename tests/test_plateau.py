#!/usr/bin/env python
# -*- coding: utf-8 -*-

from marsrover.position import Position
from marsrover.plateau import Plateau

import pytest
   

def test_illegal_plateau():
    with pytest.raises(ValueError):
        Plateau(0,0)
        
def test_ok_plateau():
    assert Plateau(1,2).max_x == 1
    assert Plateau(1,2).max_y == 2
    
def test_plateau_contains():
    assert Plateau(1,0).contains(Position(0, 0, 'W'))
    assert Plateau(1,0).contains(Position(1, 0, 'W'))
    assert Plateau(1,0).contains(Position(-1, 0, 'W')) is False
    assert Plateau(1,0).contains(Position(0, -1, 'W')) is False
    assert Plateau(1,0).contains(Position(1, 1, 'W')) is False
    assert Plateau(1,0).contains(Position(0, 1, 'W')) is False
