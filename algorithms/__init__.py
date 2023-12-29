def get_all_algorithms() -> dict:
    from algorithms import FCFS, NSJF, PSJF, NPriority, PPriority, RoundRobin

    return {
        "fcfs": FCFS,
        "preemptive_priority": PPriority,
        "nonpreemptive_priority": NPriority,
        # "preemptive_sjf": PSJF,
        "nonpreemptive_sjf": NSJF,
        "roundrobin": RoundRobin,
    }
