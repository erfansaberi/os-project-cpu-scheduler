from dataclasses import dataclass


@dataclass
class Statistics:
    throughput: float
    cpu_utilization: float
    average_waiting_time: float
    average_turnaround_time: float
    average_reponse_time: float
