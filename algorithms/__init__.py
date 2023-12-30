def get_all_algorithms() -> dict:
    from algorithms import FCFS, NSJF, PSJF, NPriority, PPriority, RoundRobin

    return {
        "FCFS": FCFS,
        "PreemptivePriority": PPriority,
        "NonpreemptivePriority": NPriority,
        "PreemptiveSJF": PSJF,
        "NonpreemptiveSJF": NSJF,
        "RoundRobin": RoundRobin,
    }
