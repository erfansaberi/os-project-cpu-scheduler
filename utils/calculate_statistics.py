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
    # Throughput = Total time / number of processes
    throughput = cpu_bursts[-1].end_time / len(processes)
    # CPU utilization = Total CPU burst time / Total time
    cpu_utilization = (
        sum(burst.end_time - burst.start_time for burst in cpu_bursts)
        / cpu_bursts[-1].end_time
    )
    # Average waiting time = Total waiting time / number of processes
    average_waiting_time = calculate_average_waiting_time(processes)
    # Average turnaround time = Total turnaround time / number of processes
    average_turnaround_time = calculate_average_turnaround_time(processes)
    # Average response time = Total response time / number of processes
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
    return 0  # TODO: Implement Average Turnaround Time calculator


def calculate_average_reponse_time(processes: list[Process]) -> float:
    return 0  # TODO: Implement Average Response Time calculator
