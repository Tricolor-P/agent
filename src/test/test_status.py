import pytest
from src.app.status import Status
from src.app.window import Window
from src.app.messages import Messages
from src.app.recorder import Recorder
from src.app.parallel_executor import ParallelExecutor

@pytest.fixture(scope='module', autouse=True)
def scope_module():
    para_exec = ParallelExecutor(cmd = "exec stdbuf -oL -eL ./../AssaultCube/assaultcube.sh")
    para_exec.start()
    print("AssaultCube start")
    yield
    para_exec.stop()
    print("AssaultCube stop")

def test_status():
    status = Status(Window("AssaultCube"), Messages(), Recorder())
    status.update()