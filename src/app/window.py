import subprocess
import cv2

class Window:
    def __init__(self, name):
        self.name = name
    def capture(self):
        cmd = ["./capture.sh", self.name]
        #cmd = ["import", "-window", self.name, "tmp.jpg"]
        # windoeが見つからない時に選択してって言われるのでreturn code 1 にならず使いづらいので棄却
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE)
            if res.returncode==1:
                raise NameError('capture failed')
        except NameError:
            raise
        else:
            return cv2.imread("tmp.jpg")
    def display(self):
        img = self.capture()
        cv2.imshow('window.name:'+self.name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
