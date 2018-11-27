import pytest
from src.app.parallel_executor import ParallelExecutor
from src.app.window import Window
import time
import numpy

@pytest.fixture(scope='module', autouse=True)
def scope_module():
    para_exec = ParallelExecutor(cmd = "exec stdbuf -oL -eL ./../AssaultCube/assaultcube.sh")
    para_exec.start()
    print("AssaultCube start")
    yield
    para_exec.stop()
    print("AssaultCube stop")

def test_window_success():
    window = Window("AssaultCube")
    img = window.capture()
    assert type(img) == numpy.ndarray

def test_window_false():
    window = Window("AAA")
    with pytest.raises(NameError):
        window.capture()

def test_window_capture_fps():
    window = Window("AssaultCube")
    start_time = time.time()
    now_time = time.time()
    cnt = 0
    while now_time  - start_time < 3.0:
        window.capture()
        cnt += 1
        now_time = time.time()
    assert cnt > 30 * 3
