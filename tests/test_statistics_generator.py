from schemas.process import Process, ProcessBurst
from schemas.report import Statistics
from utils.calculate_statistics import calculate_statistics
from utils.generate_report import generate_report


def test_statistics():
    # P1 0-24
    # P2 24-27
    # P3 27-30
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

    # SRTF, ch06, page 6.19
    # P1 0-1 & 10-17
    # P2 1-5
    # P4 5-10
    # P3 17-26
    p1 = Process("P1", 1, 0, 8)
    p2 = Process("P2", 0, 0, 4)
    p3 = Process("P3", 2, 0, 9)
    p4 = Process("P4", 3, 0, 5)
    p1.bursts = [ProcessBurst(0, 1), ProcessBurst(10, 17)]
    p2.bursts = [ProcessBurst(1, 5)]
    p3.bursts = [ProcessBurst(17, 26)]
    p4.bursts = [ProcessBurst(5, 10)]
    p1.remaining_time = 0
    p2.remaining_time = 0
    p3.remaining_time = 0
    p4.remaining_time = 0
    processes = [p1, p2, p3, p4]
    statistics = calculate_statistics(processes)
    print(statistics)
    expected_statistics = Statistics(
        throughput=0.1,
        cpu_utilization=1,
        average_waiting_time=2.5,
        average_turnaround_time=9.5,
        average_reponse_time=2.5,
    )

    # Round Robin, ch06, page 6.24
    p1 = Process("P1", 0, 0, 24)
    p2 = Process("P2", 0, 0, 3)
    p3 = Process("P3", 0, 0, 3)
    p1.bursts = [
        ProcessBurst(0, 4),
        ProcessBurst(10, 14),
        ProcessBurst(14, 18),
        ProcessBurst(18, 22),
        ProcessBurst(22, 26),
        ProcessBurst(26, 30),
    ]
    p2.bursts = [ProcessBurst(4, 7)]
    p3.bursts = [ProcessBurst(7, 10)]
    p1.remaining_time = 0
    p2.remaining_time = 0
    p3.remaining_time = 0
    processes = [p1, p2, p3]
    print(processes)
    print(calculate_statistics(processes))
    print(generate_report(processes))

    p1 = Process("P1", 0, 0, 5)
    p2 = Process("P2", 1, 0, 3)
    p3 = Process("P3", 2, 0, 1)
    p4 = Process("P4", 3, 0, 2)
    p5 = Process("P5", 4, 0, 3)
    p1.bursts = [
        ProcessBurst(0, 2),
        ProcessBurst(5, 7),
        ProcessBurst(12, 13),
    ]
    p2.bursts = [
        ProcessBurst(2, 4),
        ProcessBurst(11, 12),
    ]
    p3.bursts = [
        ProcessBurst(4, 5),
    ]
    p4.bursts = [ProcessBurst(7, 9)]
    p5.bursts = [
        ProcessBurst(9, 11),
        ProcessBurst(13, 14),
    ]
    p1.remaining_time = 0
    p2.remaining_time = 0
    p3.remaining_time = 0
    p4.remaining_time = 0
    p5.remaining_time = 0
    processes = [p1, p2, p3, p4, p5]
    statistics = calculate_statistics(processes)
    print(statistics)


test_statistics()
