from core.database import get_reading_history
import matplotlib.pylab as plt
import matplotlib.dates as mdates
from datetime import datetime

def prepare_chart_data():

    readings = get_reading_history()

    if not readings :
        print("No historical data available.")
        return [] , [] , [], []
    #oldest reading first 
    readings = readings[::-1]
    timestamps = []
    cpu_values = []
    memory_values = []
    disk_values = []

    for reading in readings:
        timestamps.append(datetime.strptime(reading[1], "%Y-%m-%d %H:%M:%S"))
        cpu_values.append(reading[2])
        memory_values.append(reading[3])
        disk_values.append(reading[4] if reading[4] is not None else float("nan"))
    return timestamps , cpu_values , memory_values , disk_values


def show_resource_dashboard():
    timestamps , cpu , memory, disk = prepare_chart_data()
    if not timestamps:
        return 
    fig , axes = plt.subplots(3,1, figsize=(9,7))
    for ax in axes :
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        ax.tick_params(axis="x", labelrotation=30)
    #cpu graph'
    axes[0].plot(timestamps, cpu , marker = "o")
    axes[0].set_title("CPU Usage History")
    axes[0].set_ylabel("Usage(%)")
    axes[0].set_xlabel("Time")
    axes[0].set_ylim(0,100)
    axes[0].grid(True)
    #RAM graph
    axes[1].plot(timestamps, memory , marker = "o")
    axes[1].set_title("Memory Usage History")
    axes[1].set_ylabel("Usage(%)")
    axes[1].set_xlabel("Time")
    axes[1].set_ylim(0,100)
    axes[1].grid(True)
    #Disk graph
    axes[2].plot(timestamps, disk , marker = "o")
    axes[2].set_title("Disk Usage History")
    axes[2].set_ylabel("Usage(%)")
    axes[2].set_xlabel("Time")
    axes[2].set_ylim(0,100)
    axes[2].grid(True)
    fig.suptitle("NEXUS - Resource Analytics")
    plt.tight_layout(pad= 2.0)
    plt.show()

if __name__ == "__main__":
    show_resource_dashboard()
