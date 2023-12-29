"""Round Robin Algorithm"""

from copy import deepcopy
from multiprocessing import current_process

from algorithms.utils import finished
from schemas.process import Process, ProcessBurst
from utils.bursts import join_bursts

TIME_QUANTUM = 2


def schedule(processes: list[Process], quantum: int = TIME_QUANTUM) -> list[Process]:
    """Round Robin Algorithm scheduler algorithm.
    This scheduler will execute the process that have arrived
    before another processes, with a given time quanum (default: 2)
    then sends them to the end of the queue.

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

        # Sort by arrival time
        ready_processes.sort(key=lambda proc: proc.arrival_time)

        # Process with the smallest given time
        smallest = min(
            ready_processes,
            key=lambda proc: proc.burst_time - proc.remaining_time,
        )
        smallest_given_time = smallest.burst_time - smallest.remaining_time

        # Filter processes with the smallest given time
        ready_processes = list(
            filter(
                lambda proc: proc.burst_time - proc.remaining_time
                == smallest_given_time,
                ready_processes,
            )
        )

        # Sort by arrival time and priority
        ready_processes.sort(key=lambda proc: (proc.arrival_time, proc.priority))

        # Get the first process
        current_process = ready_processes[0]
        current_process.bursts.append(
            ProcessBurst(
                start_time=current_time,
                end_time=current_time + quantum,
            )
        )
        current_process.remaining_time -= quantum
        current_time += quantum

    queue = join_bursts(queue)
    return queue
