"""Preemptive Priority Algorithm"""
from copy import deepcopy

from algorithms.utils import finished
from schemas.process import Process, ProcessBurst


def schedule(processes: list[Process]) -> list[Process]:
    """PP (Preemptive Priority) scheduler algorithm.
    This scheduler will execute the process with the
    lowest priority number. If there is more than one
    process with same priority number, it will execute
    the process that arrived before anothers first.

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

        smallest_priority = min(
            ready_processes,
            key=lambda proc: proc.priority,
        ).priority

        ready_processes = list(
            filter(
                lambda proc: proc.priority == smallest_priority,
                ready_processes,
            )
        )

        ready_processes.sort(key=lambda proc: proc.arrival_time)

        current_process = ready_processes[0]
        current_process.bursts.append(
            ProcessBurst(
                start_time=current_time,
                end_time=current_time + 1,
            )
        )
        current_process.remaining_time -= 1
        current_time += 1
    return queue
