"""Preemptive Shortest Job First Algorithm"""

from copy import deepcopy

from algorithms.utils import finished
from schemas.process import Process, ProcessBurst
from utils.bursts import join_bursts


def schedule(processes: list[Process]) -> list[Process]:
    """Preemptive Shortest Job First Algorithm scheduler algorithm.
    This scheduler will execute the process that have the smallest
    burst time, and if any other jobs arrived with smaller burst,
    it will preempt the current job and execute the new one.

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

        smallest_burst_time = min(
            ready_processes,
            key=lambda proc: proc.burst_time,
        ).burst_time

        ready_processes = list(
            filter(
                lambda proc: proc.burst_time == smallest_burst_time,
                ready_processes,
            )
        )
        ready_processes.sort(key=lambda proc: proc.priority)

        current_process = ready_processes[0]
        current_process.bursts.append(
            ProcessBurst(
                start_time=current_time,
                end_time=current_time + 1,
            )
        )
        current_time += 1
        current_process.remaining_time -= 1

    queue = join_bursts(queue)
    return queue
