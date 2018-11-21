import random
from .command import MoveCommand, AimCommand, NoCommand, ShotCommand

class EnableCommands():
    def __init__(self):
        self.list = []
    def random_choice(self):
        return random.choice(self.list)
    def choice(self, id):
        return self.list[id]
    def num_of_commands(self):
        return len(self.list)

class EnableMoveCommands(EnableCommands):
    def __init__(self):
        super().__init__()
        x_list = ["a", "", "d"]
        y_list = ["w", "", "s"]
        for x in x_list:
            for y in y_list:
                self.list.append(MoveCommand(x,y))

class EnableAimCommands(EnableCommands):
    def __init__(self):
        super().__init__()
        x_list = [-60,-30,  0, 30, 60]
        y_list = [ 30,  0,-30]
        for x in x_list:
            for y in y_list:
                self.list.append(AimCommand(x, y))

class EnableShotCommands(EnableCommands):
    def __init__(self):
        super().__init__()
        self.list.append(NoCommand())
        self.list.append(ShotCommand())