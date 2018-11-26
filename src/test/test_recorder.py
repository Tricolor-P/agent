import pytest
from src.app.recorder import Recorder

def test_recorder():
    recorder = Recorder()
    recorder.update_frame({"screen":"aaa.jpg"})
    recorder.update_frame({"messages":["msgaa", "msgbb"]})
    recorder.update_frame({"command":["1", "2", "3"]})
    recorder.push_frame()
    assert recorder.data = [["img", "msgs", "ops"]]