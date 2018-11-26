from abc import ABCMeta, abstractmethod

class Command(metaclass = ABCMeta):
    def __init__(self, cmd):
        self.cmd = cmd
    @abstractmethod
    def run(self):
        print(self.__class__.__name__ + ":run()")

class NoCommand(Command):
    def __init__(self):
        super().__init__("NoCommand")
    def run(self):
        super().run()
        return self.cmd

class MoveCommand(Command):
    def __init__(self, x, y):
        super().__init__("MoveCommand")
        self.x = x
        self.y = y
    def run(self):
        super().run()
        print("移動する")
        return [self.x, self.y]

class AimCommand(Command):
    def __init__(self, x, y):
        super().__init__("MouseMove")
        self.x = x
        self.y = y
    def run(self):
        super().run()
        print("マウス動かす")
        return [self.x, self.y]

class ShotCommand(Command):
    def __init__(self):
        super().__init__("Shot")
    def run(self):
        super().run()
        print("撃つ")
        return self.cmd
