import subprocess
import cv2

class Window:
    def __init__(self, name):
        self.name = name
        self.img = None
    def capture(self):
        cmd = ["./capture.sh", self.name]
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE)
            if res.returncode==1:
                raise NameError('capture failed')
        except NameError:
            raise
        else:
            self.img = cv2.imread("tmp.jpg")
    def display(self):
        cv2.imshow('window.name:'+self.name, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
