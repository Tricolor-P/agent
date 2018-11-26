
class Status:
    def __init__(self, window, messages, recorder):
        self.window = window
        self.messages = messages
        self.recorder = recorder
    def update(self):
        self.window.capture()
        self.messages.update()
        self.notify_recorder()
    def notify_recorder(self):
        self.recorder.update_frame(self.window.img)