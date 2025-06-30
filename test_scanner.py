import logging
from unittest.mock import MagicMock
from devices import stageController
from sim_devices import SimStage
from save_file import rolling_average, detect_peak
      
def test_state_retry_logic_wMock(caplog): #caplog to capture things using logging.*
    logging.basicConfig(level=logging.DEBUG)
    
    # simulate the simulated stage action
    fake_stage = SimStage()
    fake_stage.move_to = MagicMock(side_effect=[TimeoutError, TimeoutError, None]) #simulating two failures followed by no error
    
    # wrap it with retry controller
    controller = stageController(fake_stage, max_retries=3, retry_delay=0)
    
    with caplog.at_level(logging.DEBUG):
        success = controller.move_to(1, 0)
        
    # check if stage retried 3 times to move
    assert fake_stage.move_to.call_count == 3
    
    # check logs
    assert "Timeout error" in caplog.text
    assert "Moved to" in caplog.text
    
    # final result
    assert success is True
    
def test_rolling_average_basic():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rolling_average(data, 3)
    expected = [1.0, 1.5, 2.0, 3.0, 4.0]
    assert result == expected
    
def test_rolling_average_with_none():
    data = [1.0, None, 3.0, None, 5.0]
    result = rolling_average(data, 3)
    expected = [1.0, None, 2.0, None, 4.0]
    assert result == expected
    
def test_detect_peak():
    data = [(0.0, 0.0, 1.2), (1.0, 0.0, 1.1), (2.0, 0.0, 1.6)]
    filtered = [1.2, 1.15, 1.3]
    result = detect_peak(data, filtered)
    expected = [(2.0, 0.0, 1.3)]
    assert result == expected    
