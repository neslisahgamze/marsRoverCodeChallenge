#!/usr/bin/env python3
from .plateau import Plateau
from .world import World
from .rover import Rover
from .position import Position

def _turn(current_direction, turn_direction):
    if turn_direction == 'L':
        directions = ['N', 'W', 'S', 'E']
    elif turn_direction == 'R':
        directions = ['E', 'S', 'W', 'N']
    current_direction_index = directions.index(current_direction)
    new_direction_index = current_direction_index + 1
    return directions[new_direction_index % len(directions)]
   

def _move(position):
    (x, y, direction) = (position.x, position.y, position.heading)
    moves = {'N': lambda x, y: Position(x, y+1, direction),
             'W': lambda x, y: Position(x-1, y, direction),
             'S': lambda x, y: Position(x, y-1, direction),
             'E': lambda x, y: Position(x+1, y, direction),
            }
    return moves[direction](x, y)

def parse(input):
    lines = filter(lambda l: l.strip(), input.splitlines())
    max_x, max_y = next(lines).split()
    plateau = Plateau(int(max_x), int(max_y))
    world = World(plateau)
    while lines:
        try:
            x, y, heading = next(lines).split()
            instructions = next(lines)
            world.add_rover(Rover( Position(int(x), int(y), heading), plateau))
            world.add_instructions(instructions)
        except StopIteration:
            break
    return world

