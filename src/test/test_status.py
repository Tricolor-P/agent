import pytest
from src.app.status import Status
from src.app.window import Window
from src.app.record import RoundRecord
from src.app.parallel_executor import ParallelExecutor

@pytest.fixture(scope='module', autouse=True)
def para_exec():
    para_exec = ParallelExecutor(cmd = "exec stdbuf -oL -eL ./../AssaultCube/assaultcube.sh")
    para_exec.start()
    print("AssaultCube start")
    yield para_exec
    para_exec.stop()
    print("AssaultCube stop")

def test_status(para_exec):
    round_record = RoundRecord()
    status = Status(Window("AssaultCube"), para_exec, round_record)
    status.update()
    round_record.current_frame.write("tmp/test_status_current_frame.json")