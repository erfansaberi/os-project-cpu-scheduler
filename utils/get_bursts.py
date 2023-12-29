from schemas.process import Process


def get_bursts(processes: list[Process]) -> list[tuple[str, int, int]]:
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
