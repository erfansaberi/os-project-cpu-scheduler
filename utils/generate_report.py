from schemas.process import Process
from schemas.report import Statistics
from utils.calculate_statistics import calculate_statistics


def generate_report(
    processes: list[Process], statistics: Statistics | None = None
) -> str:
    if not statistics:
        statistics = calculate_statistics(processes)
    report = f"{statistics.throughput}\n"
    report += f"{statistics.cpu_utilization*100}%\n"
    report += f"{statistics.average_waiting_time}\n"
    report += f"{statistics.average_turnaround_time}\n"
    report += f"{statistics.average_reponse_time}\n"
    for process in processes:
        log = f"{process.id}"
        for burst in process.bursts:
            log += f", {burst.start_time}, {burst.end_time}"
        report += f"{log}\n"
    return report
