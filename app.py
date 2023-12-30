"""
OS CPU Scheduler Algorithms Simulator
Author: Erfan Saberi
Date: Dec 2023

This app will read a list of processes  from list.txt  file
and runs cpu scheduler algorithms for them, then calculates
statistics for each algorithm and writes a report in a file
with the algorithm name in output/ directory.

Usage: python3 app.py
"""
# OS CPU Schedulers Simulator & Calculator
# Read input from list.txt -> Put in Data classes (Process)
# Run the simulation for each algorithm -> Output the results
# Save the results in seperated files
# Statistics: Throughput, CPU Utilization, Average Waiting Time, Average Turnaround Time, Average Response Time
# Output: Statistics, Processes (ID, Start1, End1, Start2, End2, Start3, End3, Start4, End4, Start5, End5, ...)

import sys

if len(sys.argv) < 2:
    print(
        "Use 'python3 app.py gui' to run the GUI "
        "or 'python3 app.py execute' to run the algorithms and generate reports"
    )
elif sys.argv[1] == "gui":
    from gui.gui import GUI

    GUI()
elif sys.argv[1] == "execute":
    import os

    from algorithms import get_all_algorithms
    from utils.generate_report import generate_report
    from utils.input_parser import parse_input_data

    if not os.path.exists("reports/"):
        os.mkdir("reports/")

    with open("list.txt") as file:
        print("Reading data from list.txt")
        data = parse_input_data(file.read())

    for algorithm_name, algorithm in get_all_algorithms().items():
        print(f"Scheduling by {algorithm_name} algorithm...", end="", flush=True)
        sch = algorithm.schedule(data)
        report = generate_report(sch)
        with open(f"reports/{algorithm_name}.txt", "w") as report_file:
            report_file.write(report)
        print("Done!")

    print("Finished")
else:
    print(f"Invalid command {sys.argv[1]}")
    print("Use 'python3 app.py gui' to run the GUI")
    print("or 'python3 app.py execute' to run the algorithms and generate reports")
