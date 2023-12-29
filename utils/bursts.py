from copy import deepcopy

from schemas.process import Process, ProcessBurst


def join_bursts(processes: list[Process]) -> list[Process]:
    """Join bursts of processes

    Args:
        processes (list[Process]): List of processes

    Returns:
        list[Process]: List of processes with joined bursts
    """
    queue = deepcopy(processes)
    for process in queue:
        process_bursts = process.bursts
        joined_bursts: list[ProcessBurst] = []
        for burst in process_bursts:
            if not joined_bursts:
                joined_bursts.append(burst)
                continue
            last_burst = joined_bursts[-1]
            if last_burst.end_time == burst.start_time:
                last_burst.end_time = burst.end_time
            else:
                joined_bursts.append(burst)
        process.bursts = joined_bursts
    return queue


def get_bursts_as_list(processes: list[Process]) -> list[tuple[str, int, int]]:
    """Get the bursts of processes

    Args:
        processes (list[Process]): List of processes

    Returns:
        tuple: List of bursts
    """
    bursts = []
    for process in processes:
        for burst in process.bursts:
            bursts.append((process.id, burst.start_time, burst.end_time))
    bursts.sort(key=lambda burst: burst[1])
    return bursts
