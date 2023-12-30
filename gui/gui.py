from venv import create

import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import algorithms
from algorithms import get_all_algorithms
from utils.bursts import get_bursts_as_list
from utils.generate_report import generate_report
from utils.input_parser import parse_input_data


class GUI:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        self.root.title("CPU Scheduler Simulator")
        self.root.geometry("800*600")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Left Frame
        self.leftframe = customtkinter.CTkFrame(self.root)
        self.leftframe.pack(
            pady=20, padx=10, fill="both", expand=True, side=customtkinter.LEFT
        )

        # Input Textbox
        self.inputlabel = customtkinter.CTkLabel(self.leftframe, text="Input:")
        self.inputlabel.pack(pady=5, padx=10)
        self.inputtextbox = customtkinter.CTkTextbox(self.leftframe)
        self.inputtextbox.pack(padx=10, fill="both", expand=True)

        # Output Textbox
        self.outputlabel = customtkinter.CTkLabel(self.leftframe, text="Report:")
        self.outputlabel.pack(pady=5, padx=10)
        self.outputtextbox = customtkinter.CTkTextbox(self.leftframe)
        self.outputtextbox.configure(state="disabled")
        self.outputtextbox.pack(pady=5, padx=10, fill="both", expand=True)

        # Run Button
        self.runbutton = customtkinter.CTkButton(
            self.leftframe, text="Run", command=self.run
        )
        self.runbutton.pack(pady=10, padx=10)

        # Right Frame
        self.rightframe = customtkinter.CTkFrame(self.root)
        self.rightframe.pack(
            pady=20, padx=10, fill="both", expand=True, side=customtkinter.RIGHT
        )

        # Gantt Chart
        self.gantt_chart = plt.Figure()
        self.gantt_chart.patch.set_facecolor("#404040")  # TODO: Use customtkinter color
        self.gantt_chart_widget = FigureCanvasTkAgg(self.gantt_chart, self.rightframe)
        self.gantt_chart_widget.get_tk_widget().pack(fill="both", expand=True)

        # Gantt Chart Toolbar
        self.gantt_chart_toolbar = NavigationToolbar2Tk(
            self.gantt_chart_widget, self.rightframe
        )
        self.gantt_chart_toolbar.pack

        # Algorithm Selection
        self.algorithms = get_all_algorithms()
        self.algorithms_combobox = customtkinter.CTkComboBox(
            self.rightframe, values=list(self.algorithms.keys())
        )
        self.algorithms_combobox.pack(pady=10, padx=10, fill="both")

    def create_gantt_chart(self, bursts):
        self.gantt_chart.clear()
        ax = self.gantt_chart.add_subplot(111)

        process_lines = {}
        for burst in bursts:
            task_name = burst[0]
            start_time = burst[1]
            end_time = burst[2]

            if task_name in process_lines:
                line_number = process_lines[task_name]
            else:
                line_number = len(process_lines)
                process_lines[task_name] = line_number

            ax.broken_barh(
                [(start_time, end_time - start_time)],
                (10 * line_number, 9),
                facecolors="tab:blue",
            )
            ax.text(
                start_time + (end_time - start_time) / 2,
                10 * line_number + 4.5,
                task_name,
                ha="center",
                va="center",
            )

        ax.set_xlabel("Time")
        ax.set_ylabel("Processes")
        ax.set_yticks([10 * i + 5 for i in range(len(process_lines))])
        ax.set_yticklabels(list(process_lines.keys()))

        self.gantt_chart_widget.draw()

    def run(self):
        # Run Algorithm
        data = parse_input_data(self.inputtextbox.get("1.0", "end-1c"))
        algorithm = self.algorithms[self.algorithms_combobox.get()]
        schedule = algorithm.schedule(data)
        report = generate_report(schedule)

        # Write Report
        self.outputtextbox.configure(state="normal")
        self.outputtextbox.delete("0.0", "end-1c")
        self.outputtextbox.insert("0.0", report)
        self.outputtextbox.configure(state="disabled")

        # Draw Gantt Chart
        bursts = get_bursts_as_list(schedule)
        self.create_gantt_chart(bursts)


GUI()
