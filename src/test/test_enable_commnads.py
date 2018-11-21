import pytest
from src.app.enable_commands import EnableMoveCommands, EnableAimCommands, EnableShotCommands

def test_enable_move_commands():
    assert 9 == EnableMoveCommands().num_of_commands()
    assert ["a", "w"] == EnableMoveCommands().choice(0).run()
    assert [ "", ""] == EnableMoveCommands().choice(4).run()

def test_aim_commands():
    assert 15 == EnableAimCommands().num_of_commands()
    assert [-60, 30] == EnableAimCommands().choice(0).run()
    assert [  0,  0] == EnableAimCommands().choice(7).run()

def test_shot_commands():
    assert 2 == EnableShotCommands().num_of_commands()
    assert "NoCommand" == EnableShotCommands().choice(0).run()
    assert "Shot" == EnableShotCommands().choice(1).run()

