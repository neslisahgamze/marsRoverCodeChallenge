#!/usr/bin/env python
# -*- coding: utf-8 -*-

from marsrover.plateau import Plateau
from marsrover.cli import main, parse
 
def test_parse_input():
    input = """\
5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM
"""
    world = parse(input)
    assert world.plateau == Plateau(5,5)
    assert str(world.rovers) == "[Rover(Position(x=1, y=2, heading='N'), Plateau(max_x=5, max_y=5)), Rover(Position(x=3, y=3, heading='E'), Plateau(max_x=5, max_y=5))]"
    assert str(world.instructions) == "['LMLMLMLMM', 'MMRMMRMRRM']"
    
def test_main():
    input = """\
5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM
"""
    output = main(input)
    expected_output = """\
1 3 N

5 1 E
"""
    assert output == expected_output
