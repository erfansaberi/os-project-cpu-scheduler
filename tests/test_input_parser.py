from schemas.process import Process
from utils.input_parser import parse_input_data


def test_parse_input_data():
    input_data = "P1, 10, 0, 5\nP2, 5, 1, 3\nP3, 8, 0, 4"
    expected_output = [
        Process(id="P1", arrival_time=10, priority=0, burst_time=5),
        Process(id="P2", arrival_time=5, priority=1, burst_time=3),
        Process(id="P3", arrival_time=8, priority=0, burst_time=4),
    ]

    assert parse_input_data(input_data) == expected_output
