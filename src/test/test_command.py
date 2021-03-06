import pytest
from src.app.command import Command, NoCommand, MoveCommand, AimCommand, ShotCommand

def test_command_init():
    assert "NoCommand" == NoCommand().run()

def test_move_commnad():
    assert ["d", ""] == MoveCommand( "d","").run()
    assert [ "","s"] == MoveCommand(  "","s").run()
    assert ["a","w"] == MoveCommand( "a","w").run()


def test_aim_command():
    assert [ 1, 1] == AimCommand(1, 1).run()
    assert [ 0, 0] == AimCommand(0, 0).run()
    assert [-1,-1] == AimCommand(-1, -1).run()

def test_shot_command():
    assert "Shot" == ShotCommand().run()
