"""Non-preemptive Shortest Job First Algorithms"""
from copy import deepcopy

from algorithms.utils import finished
from schemas.process import Process, ProcessBurst


def schedule(processes: list[Process]) -> list[Process]:
    """Non-preemptive Shortest Job First scheduler algorithm.
    This scheduler will execute the processes that have
    the shortest burst time first. If there is more
    than one process with same burst time, it will
    execute the process that has the smallest priority number.

    Args:
        processes (list[Process]): List of processes to schedule

    Returns:
        list[Process]: List of scheduled processes
    """
    queue = deepcopy(processes)
    current_time = 0
    current_process = None
    while not finished(queue):
        # Filter arrived and unfinished processes
        ready_processes = list(
            filter(
                lambda proc: proc.arrival_time <= current_time
                and proc.remaining_time > 0,
                queue,
            )
        )

        # Not any arrived processes
        if not ready_processes:
            current_time += 1
            continue

        shortest_burst = min(
            ready_processes,
            key=lambda proc: proc.burst_time,
        ).burst_time

        ready_processes = list(
            filter(
                lambda proc: proc.burst_time == shortest_burst,
                ready_processes,
            )
        )

        ready_processes.sort(key=lambda proc: proc.priority)

        current_process = ready_processes[0]
        current_process.bursts.append(
            ProcessBurst(
                start_time=current_time,
                end_time=current_time + current_process.burst_time,
            )
        )
        current_process.remaining_time = 0
        current_time += current_process.burst_time

    return queue
