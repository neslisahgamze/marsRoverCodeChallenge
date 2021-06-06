import sys
import os
sys.path.append(os.path.realpath('.'))

from marsrover.plateau import Plateau
from marsrover.world import World
from marsrover.rover import Rover
from marsrover.position import Position

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


def main(input):
    world = parse(input)
    world.follow_instructions()
    output = "\n".join([rover.report_position() for rover in world.rovers])
    return output


if __name__ == "__main__":
    input = sys.stdin.read()
    output = main(input)
    print(output)
