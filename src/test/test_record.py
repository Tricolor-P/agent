import pytest
from src.app.record import ScreenRecord, MessageRecord, CommandRecord, FrameRecord, RoundRecord
import time

class TestScreenRecord:
    def test_record(self):
        screen_record = ScreenRecord("screen001.jpg", "numpy img array")
        screen_record.dump()
        assert screen_record.name == "screen001.jpg"
        assert screen_record.img == "numpy img array"

    def test_write(self):
        screen_record = ScreenRecord("screen001.jpg", "numpy img array")
        screen_record.write("tmp/test_screen_record.json")

    def test_read(self):
        screen_record = ScreenRecord.read("tmp/test_screen_record.json")
        assert screen_record.name == "screen001.jpg"
        assert screen_record.img == "numpy img array"


class TestMessageRecord:
    def test_record(self):
        message_record = MessageRecord(["aa", "bb"])
        message_record.dump()
        assert message_record.msgs == ["aa", "bb"]

    def test_write(self):
        message_record = MessageRecord(["aa", "bb"])
        message_record.write("tmp/test_message_record.json")

    def test_read(self):
        message_record = MessageRecord.read("tmp/test_message_record.json")
        assert message_record.msgs == ["aa", "bb"]


class TestCommandRecord:
    def test_record(self):
        command_record =  CommandRecord("move_cmd", "aim_cmd", "shot_cmd")
        command_record.dump()
        assert command_record.move == "move_cmd"
        assert command_record.aim  == "aim_cmd"
        assert command_record.shot == "shot_cmd"

    def test_write(self):
        command_record =  CommandRecord("move_cmd", "aim_cmd", "shot_cmd")
        command_record.write("tmp/test_command_record.json")

    def test_read(self):
        command_record = CommandRecord.read("tmp/test_command_record.json")
        assert command_record.move == "move_cmd"
        assert command_record.aim  == "aim_cmd"
        assert command_record.shot == "shot_cmd"


class TestFrameRecord:
    def test_record(self):
        index = 1
        time = 0.1
        frame_record = FrameRecord(index, time)
        frame_record.dump()
        assert frame_record.index == index
        assert frame_record.time == time

    def test_add(self):
        index = 2
        time = 0.5
        frame_record = FrameRecord(index, time)
        frame_record.add("key1", "value1")
        frame_record.add("key2", "value2")
        frame_record.add("key3", "value3")
        frame_record.dump()
    
    def test_write(self):
        index = 2
        time = 0.5
        frame_record = FrameRecord(index, time)
        frame_record.add("screen",  ScreenRecord("screen001.jpg", "numpy img array"))
        frame_record.add("message", MessageRecord(["aa", "bb"]))
        frame_record.add("command", CommandRecord("move_cmd", "aim_cmd", "shot_cmd"))
        frame_record.write("tmp/test_frame_record.json")
    
    def test_read(self):
        frame_record = FrameRecord.read("tmp/test_frame_record.json")
        assert type(frame_record.data["screen"]) is ScreenRecord
        assert type(frame_record.data["message"]) is MessageRecord
        assert type(frame_record.data["command"]) is CommandRecord


class TestRoundRecord:
    def test_write(self):
        round_record = RoundRecord()
        for i in range(3):
            round_record.update_status("numpy img array", ["msg{}-1".format(i), "msg{}-2".format(i)])
            round_record.update_commnad("move_cmd{}".format(i),
                                        "aim_cmd{}".format(i),
                                        "shot_cmd{}".format(i))
            time.sleep(0.1)
        round_record.dump()
        round_record.write("tmp/test_round_record.json")
        assert type(round_record) is RoundRecord
    
    def test_read(self):
        round_record = RoundRecord.read("tmp/test_round_record.json")
        assert type(round_record.frames[0]) is FrameRecord


