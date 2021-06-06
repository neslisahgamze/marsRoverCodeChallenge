class World:
    def __init__(self, plateau):
        self.plateau = plateau
        self.rovers = []
        self.instructions = []
        
    def add_rover(self, rover):
        self.rovers.append(rover)
        
    def add_instructions(self, instructions):
        self.instructions.append(instructions)
        
    def follow_instructions(self):
        for index, rover in enumerate(self.rovers):
            instructions = self.instructions[index]
            for c in instructions:
                if c == 'M':
                    rover.move()
                elif c in ['L', 'R']:
                    rover.turn(c)
