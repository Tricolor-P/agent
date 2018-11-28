"""
#課題、
"""

class Status:
    def __init__(self, window, para_exec, round_record ):
        self.img = None
        self.msgs = None
        self.window = window
        self.para_exec = para_exec
        self.round_record = round_record
    def update(self):
        self.img = self.window.capture()
        self.msgs = self.para_exec.dump()
        self.notify_recorder()
    def notify_recorder(self):
        self.round_record.update_status(self.img, self.msgs)