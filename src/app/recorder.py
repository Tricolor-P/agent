class Recorder:
    def __init__(self):
        self.data = []
    def update_frame(self, img):
        self.data.append(img)