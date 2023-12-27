from schemas.process import Process
from schemas.report import Statistics
from utils.calculate_statistics import calculate_statistics


def generate_report(
    processes: list[Process], statistics: Statistics | None = None
) -> str:
    """Generate report from processes and statistics

    Args:
        processes (list[Process]): _description_
        statistics (Statistics | None, optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    if not statistics:
        statistics = calculate_statistics(processes)
    report = f"Throughput: {statistics.throughput}\n"
    report += f"CPU Utilization: {statistics.cpu_utilization*100}%\n"
    report += f"Avg Waiting Time: {statistics.average_waiting_time}\n"
    report += f"Avg Turnaround Time: {statistics.average_turnaround_time}\n"
    report += f"Avg Response Time: {statistics.average_reponse_time}\n"
    for process in processes:
        log = f"{process.id}"
        for burst in process.bursts:
            log += f", {burst.start_time}, {burst.end_time}"
        report += f"{log}\n"
    return report
