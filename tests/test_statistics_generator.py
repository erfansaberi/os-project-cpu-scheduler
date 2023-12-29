from schemas.process import Process, ProcessBurst
from schemas.report import Statistics
from utils.calculate_statistics import calculate_statistics


def test_statistics():
    # TODO: Write more tests

    p1 = Process("P1", 0, 0, 24)
    p2 = Process("P2", 0, 0, 3)
    p3 = Process("P3", 0, 0, 3)
    p1.bursts = [ProcessBurst(0, 24)]
    p2.bursts = [ProcessBurst(24, 27)]
    p3.bursts = [ProcessBurst(27, 30)]
    p1.remaining_time = 0
    p2.remaining_time = 0
    p3.remaining_time = 0
    processes = [p1, p2, p3]
    statistics = calculate_statistics(processes)
    expected_statistics = Statistics(
        throughput=0.1,
        cpu_utilization=1.0,
        average_waiting_time=17.0,
        average_turnaround_time=27.0,
        average_reponse_time=17.0,
    )
    assert statistics == expected_statistics


test_statistics()
