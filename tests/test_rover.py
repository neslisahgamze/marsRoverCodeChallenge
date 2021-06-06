#!/usr/bin/env python
# -*- coding: utf-8 -*-

from marsrover.rover import Rover, _turn, _move
from marsrover.position import Position
from marsrover.plateau import Plateau

import pytest

def test_turn_left():
    assert _turn('N', 'L') == 'W'
    assert _turn('W', 'L') == 'S'
    assert _turn('S', 'L') == 'E'
    assert _turn('E', 'L') == 'N'    
    

def test_turn_right():
    assert _turn('N', 'R') == 'E'
    assert _turn('W', 'R') == 'N'
    assert _turn('S', 'R') == 'W'
    assert _turn('E', 'R') == 'S'    
 

def test_move():
    assert _move( Position(1,2,'N') ) == Position(1,3,'N')
    assert _move( Position(1,2,'W')) == Position(0,2,'W')
    assert _move( Position(1,2,'S')) == Position(1,1,'S')
    assert _move( Position(1,2,'E')) == Position(2,2,'E')

def test_move_rover_over_edge():
    plateau = Plateau(0,1)
    rover = Rover( Position(0,1,'N'), plateau)
    with pytest.raises(ValueError):
        rover.move()

def test_move_rover_on_plateau():
    plateau = Plateau(5,5)
    rover = Rover( Position(1,2,'N'), plateau)
    rover.move()
    assert rover.position == Position(1,3, 'N')
  
def test_report_position():
    plateau = Plateau(0,1)
    rover = Rover( Position(0,1,'N'), plateau)
    assert "0 1 N\n" == rover.report_position()
