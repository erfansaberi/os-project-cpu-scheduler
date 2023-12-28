from schemas.process import Process


def finished(processes: list[Process]) -> bool:
    for p in processes:
        if p.remaining_time > 0:
            return False
    return True
