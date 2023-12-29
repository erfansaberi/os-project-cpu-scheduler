from algorithms import NPriority
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
        ("P5", 14, 24),
        ("P3", 24, 49),
        ("P4", 49, 64),
        ("P1", 64, 84),
    ]

    scheduled_queue = NPriority.schedule(sample_data)

    burst_queue = []
    for proc in scheduled_queue:
        for burst in proc.bursts:
            burst_queue.append((proc.id, burst.start_time, burst.end_time))
    burst_queue.sort(key=lambda burst: burst[1])

    assert burst_queue == expected_burst_queue
