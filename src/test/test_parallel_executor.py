import time
import pytest
from src.app.parallel_executor import ParallelExecutor

def test_parallel_executor(capsys):
    para_exec = ParallelExecutor(cmd = "exec stdbuf -oL -eL ./../AssaultCube/assaultcube.sh")
    para_exec.start()
    para_exec.stop()
    assert para_exec.dump()[0] == "Using home directory: /home/y_ozawa/.assaultcube_v1.2"
