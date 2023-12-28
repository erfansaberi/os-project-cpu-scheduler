from copy import deepcopy

from algorithms.utils import finished
from schemas.process import Process, ProcessBurst


def schedule(processes: list[Process]) -> list[Process]:
    """FCFS (First Came First Served)  scheduler  algorithm.
    This scheduler will execute the  processes  that arrived
    before anothers first. If there is more than one process
    with same arrival time, it will execute the process with
    smaller priority number.

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

        smallest_arrival_time = min(
            ready_processes,
            key=lambda proc: proc.arrival_time,
        ).arrival_time

        ready_processes = list(
            filter(
                lambda proc: proc.arrival_time == smallest_arrival_time,
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
