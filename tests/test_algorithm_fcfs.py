from algorithms import FCFS
from schemas.process import Process


def test_algorithm_fcfs():
    sample_data = [
        Process(id="P1", arrival_time=0, priority=4, burst_time=20),
        Process(id="P2", arrival_time=0, priority=2, burst_time=14),
        Process(id="P3", arrival_time=1, priority=3, burst_time=25),
        Process(id="P4", arrival_time=2, priority=3, burst_time=15),
        Process(id="P5", arrival_time=4, priority=0, burst_time=10),
    ]
    expected_burst_queue = [
        ("P2", 0, 14),
        ("P1", 14, 34),
        ("P3", 34, 59),
        ("P4", 59, 74),
        ("P5", 74, 84),
    ]

    scheduled_queue = FCFS.schedule(sample_data)

    burst_queue = []
    for proc in scheduled_queue:
        for burst in proc.bursts:
            burst_queue.append((proc.id, burst.start_time, burst.end_time))
    burst_queue.sort(key=lambda burst: burst[1])

    assert burst_queue == expected_burst_queue
