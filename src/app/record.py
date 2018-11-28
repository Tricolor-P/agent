"""
課題：ファイル読み込みの際に、dfの読み込み部分とdfからの復元部分に分けると、再帰的にかけて綺麗になる
"""

from abc import ABCMeta, abstractmethod, abstractstaticmethod
import pprint
import json
import time
from collections import OrderedDict

class Record(metaclass=ABCMeta):
    @abstractmethod
    def to_dict(self):
        pass
    @abstractstaticmethod
    def read(self, filename):
        pass
    def write(self, filename):
        with open (filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
    def dump(self):
        print(json.dumps(self.to_dict(), indent=4))


class RoundRecord(Record):
    def __init__(self):
        self.start_time = time.time()
        self.frames = []
        self.current_frame = None

    def new_frame(self):
        return FrameRecord(len(self.frames), time.time()-self.start_time)
    def fix_frame(self):
        self.frames.append(self.current_frame)

    def update_status(self, img, msgs):
        self.current_frame = self.new_frame()
        screen = ScreenRecord("screen{:03}.jpg".format(self.current_frame.index), img)
        message = MessageRecord(msgs)
        self.current_frame.add("screen", screen)
        self.current_frame.add("message", message)
    def update_commnad(self, move, aim, shot):
        self.current_frame.add("command", CommandRecord(move, aim, shot))
        self.frames.append(self.current_frame)

    def to_dict(self):
        out_list = []
        for frame in self.frames:
            out_list.append( frame.to_dict() )
        return out_list
    @staticmethod
    def read(filename):
        with open(filename, "r") as f:
            df_round = json.load(f)
            round_record = RoundRecord()
            for df in df_round:
                frame_record = FrameRecord(df["index"], df["time"])
                frame_record.add(  "screen", ScreenRecord( df["screen"]["name"] , df["screen"]["img"] ))
                frame_record.add( "message", MessageRecord( df["message"] ))
                frame_record.add( "command", CommandRecord( df["command"]["move"], df["command"]["aim"], df["command"]["shot"] ))
                round_record.frames.append(frame_record)
            return round_record



class FrameRecord(Record):
    def __init__(self, index, time):
        self.index = index
        self.time = time
        self.data = OrderedDict()
    def to_dict(self):
        dc = OrderedDict([( "index", self.index ),
                          (  "time", self.time  )])
        for key in self.data.keys():
            dc[key] = self._get_value(self.data[key])
        return dc
    def _get_value(self, obj):
        if isinstance(obj, Record):
            return obj.to_dict()
        else:
            return obj
    def add(self, key, value):
        self.data[key] = value
    @staticmethod
    def read(filename):
        with open (filename, "r") as f:
            df = json.load(f)
            frame_record = FrameRecord(df["index"], df["time"])
            frame_record.add(  "screen", ScreenRecord( df["screen"]["name"] , df["screen"]["img"] ))
            frame_record.add( "message", MessageRecord( df["message"] ))
            frame_record.add( "command", CommandRecord( df["command"]["move"], df["command"]["aim"], df["command"]["shot"] ))
            return frame_record

class ScreenRecord(Record):
    def __init__(self, name, img):
        self.name = name
        self.img  = img
    def to_dict(self):
        return OrderedDict([( "name", self.name ),
                            (  "img", self.img  )])
    @staticmethod
    def read(filename):
        with open (filename, "r") as f:
            df = json.load(f)
            return ScreenRecord(df["name"], df["img"])

class MessageRecord(Record):
    def __init__(self, msgs):
        self.msgs = msgs
    def to_dict(self):
        return self.msgs
    @staticmethod
    def read(filename):
        with open (filename, "r") as f:
            df = json.load(f)
            return MessageRecord(df)

class CommandRecord(Record):
    def __init__(self, move, aim, shot):
        self.move = move
        self.aim = aim
        self.shot = shot
    def to_dict(self):
        return OrderedDict([( "move", self.move ),
                            (  "aim", self.aim  ),
                            ( "shot", self.shot )])
    @staticmethod
    def read(filename):
        with open (filename, "r") as f:
            df = json.load(f)
            return CommandRecord(df["move"], df["aim"], df["shot"])



