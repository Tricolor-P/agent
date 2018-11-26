import time
import subprocess
import codecs
from multiprocessing import Process, Queue

class ParallelExecutor:
    def __init__(self, *,cmd=None):
        self.cmd = cmd
        self.proc = None
        self.q = Queue()
        self.p = Process(target=self._stdout2q, args=())
    def _stdout2q(self):
        while True:
            line = self.proc.stdout.readline()
            if line:
                self.q.put(codecs.decode(line)[:-1])
            if not line and self.proc.poll() is not None:
                break
    def start(self):
        self.proc = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        self.p.start()
        time.sleep(2)
    def stop(self):
        self.proc.terminate()
        self.p.terminate()
        time.sleep(1)
    def dump(self):
        res = []
        while not self.q.empty():
            res.append(self.q.get())
        return res
        