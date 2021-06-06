#!/usr/bin/env python
# -*- coding: utf-8 -*-

from marsrover.rover import Rover
from marsrover.position import Position
from marsrover.plateau import Plateau
from marsrover.world import World

def test_move_world():
    rovers = [Rover(Position(x=1, y=2, heading='N'), Plateau(max_x=5, max_y=5)), Rover(Position(x=3, y=3, heading='E'), Plateau(max_x=5, max_y=5))]
    world = World(Plateau(5, 5))
    world.rovers = rovers
    world.instructions = ["LMLMLMLMM", "MMRMMRMRRM"]
    world.follow_instructions()
    assert world.rovers[0].position == Position(1, 3, 'N')
    assert world.rovers[1].position == Position(5, 1, 'E')