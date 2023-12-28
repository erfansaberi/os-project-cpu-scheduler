from copy import deepcopy

from algorithms.utils import finished
from schemas.process import Process, ProcessBurst


def schedule(processes: list[Process]) -> list[Process]:
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
