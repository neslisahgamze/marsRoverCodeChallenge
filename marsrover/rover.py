from dataclasses import dataclass
from marsrover.plateau import Plateau
from marsrover.position import Position
from marsrover.world import World


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

class Rover:
    def __init__(self, position, plateau):
        self.position = position
        self.plateau = plateau
        
    def move(self):
        new_position = _move(self.position)
        if not self.plateau.contains(new_position):
            raise ValueError(f"Cannot move to {new_position} since it is off edge of plateau")
        self.position = new_position        

    def turn(self, direction):
        new_heading = _turn(self.position.heading, direction)
        self.position = Position(self.position.x, self.position.y, new_heading)
        
    def __repr__(self):
        return f"Rover({self.position}, {self.plateau})"
    
    def report_position(self):
        return f"{self.position.x} {self.position.y} {self.position.heading}\n"
