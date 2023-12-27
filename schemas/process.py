from dataclasses import dataclass, field


@dataclass
class ProcessBurst:
    start_time: int
    end_time: int


@dataclass
class Process:
    id: int
    arrival_time: int
    priority: int
    burst_time: int
    remaining_time: int = field(init=False)
    bursts: list[ProcessBurst] = field(init=False)

    def __post_init__(self):
        self.remaining_time = self.burst_time
        self.bursts = []
