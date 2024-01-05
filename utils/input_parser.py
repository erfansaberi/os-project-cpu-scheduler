from schemas.process import Process


def parse_input_data(input_data: str) -> list[Process]:
    """Read input data and parse it, then return a list of processes.

    Args:
        input_data (str): Input data containing
        Name, Arrival time, Priority, CPU burst
        for every process on each row.

    Returns:
        list[Process]: Parsed data in Process schema
    """
    data = input_data.splitlines()
    processes = []
    for row in data:
        pid, arrival_time, prioroty, burst_time = row.split(",")
        processes.append(
            Process(
                id=pid,
                arrival_time=int(arrival_time),
                priority=int(prioroty),
                burst_time=int(burst_time),
            )
        )
    return processes
