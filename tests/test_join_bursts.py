from schemas.process import Process, ProcessBurst
from utils.bursts import join_bursts


def test_join_bursts():
    processes = [
        Process(id="P1", arrival_time=0, priority=0, burst_time=7),
        Process(id="P2", arrival_time=5, priority=1, burst_time=2),
        Process(id="P3", arrival_time=8, priority=0, burst_time=3),
    ]
    processes[0].bursts = [
        ProcessBurst(start_time=0, end_time=3),
        ProcessBurst(start_time=3, end_time=6),
        ProcessBurst(start_time=8, end_time=9),
    ]
    processes[1].bursts = [
        ProcessBurst(start_time=7, end_time=8),
    ]
    processes[2].bursts = [
        ProcessBurst(start_time=9, end_time=10),
        ProcessBurst(start_time=10, end_time=11),
        ProcessBurst(start_time=11, end_time=12),
    ]

    expected_output = [
        Process(id="P1", arrival_time=0, priority=0, burst_time=7),
        Process(id="P2", arrival_time=5, priority=1, burst_time=2),
        Process(id="P3", arrival_time=8, priority=0, burst_time=3),
    ]
    expected_output[0].bursts = [
        ProcessBurst(start_time=0, end_time=6),
        ProcessBurst(start_time=8, end_time=9),
    ]
    expected_output[1].bursts = [
        ProcessBurst(start_time=7, end_time=8),
    ]
    expected_output[2].bursts = [
        ProcessBurst(start_time=9, end_time=12),
    ]

    joined_bursts = join_bursts(processes)

    assert joined_bursts == expected_output
