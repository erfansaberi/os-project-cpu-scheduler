from schemas.process import Process, ProcessBurst
from schemas.report import Statistics


def calculate_statistics(processes: list[Process]) -> Statistics:
    """Calculate statistics for a list of processes.

    Args:
        processes (list[Process]): List of processes

    Returns:
        Statistics: Statistics for the list of processes
    """

    # Get all CPU bursts from all processes and sort them by start time
    cpu_bursts: list[ProcessBurst] = []
    for process in processes:
        cpu_bursts.extend(process.bursts)
    cpu_bursts.sort(key=lambda burst: burst.start_time)

    # Calculate statistics
    # Throughput = Number of processes / Total time
    throughput = len(processes) / cpu_bursts[-1].end_time
    # CPU utilization = Total CPU burst time / Total time
    cpu_utilization = (
        sum(burst.end_time - burst.start_time for burst in cpu_bursts)
        / cpu_bursts[-1].end_time
    )
    average_waiting_time = calculate_average_waiting_time(processes)
    average_turnaround_time = calculate_average_turnaround_time(processes)
    average_reponse_time = calculate_average_reponse_time(processes)

    return Statistics(
        throughput=throughput,
        cpu_utilization=cpu_utilization,
        average_waiting_time=average_waiting_time,
        average_turnaround_time=average_turnaround_time,
        average_reponse_time=average_reponse_time,
    )


def calculate_average_waiting_time(processes: list[Process]) -> float:
    """Calculate average waiting time for a list of processes.

    Args:
        processes (list[Process]): List of processes

    Returns:
        float: Average waiting time for the list of processes
    """

    total_waiting_time = 0
    for process in processes:
        arrival_time = process.arrival_time
        for burst in process.bursts:
            total_waiting_time += burst.start_time - arrival_time
            arrival_time = burst.end_time

    return total_waiting_time / len(processes)


def calculate_average_turnaround_time(processes: list[Process]) -> float:
    """Calculate average turnaround time for a list of processes.

    Args:
        processes (list[Process]): List of processes

    Returns:
        float: Average turnaround time for the list of processes
    """
    total_turnaround_time = 0
    for process in processes:
        arrival_time = process.arrival_time
        for burst in process.bursts:
            total_turnaround_time += burst.end_time - arrival_time
            arrival_time = burst.end_time
    return total_turnaround_time / len(processes)


def calculate_average_reponse_time(processes: list[Process]) -> float:
    """Calculate average response time for a list of processes.

    Args:
        processes (list[Process]): List of processes

    Returns:
        float: Average response time for the list of processes
    """
    total_response_time = 0
    for process in processes:
        first_burst = process.bursts[0]
        total_response_time += first_burst.start_time - process.arrival_time
    return total_response_time / len(processes)
