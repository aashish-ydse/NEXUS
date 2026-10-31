import platform
import os
import psutil

def get_system_info():
    info = {
        "OS" : platform.system(),
        "Machine" : platform.machine(),
        "Python" : platform.python_version(),
        "CPU cores" : os.cpu_count(),
        "CPU Usage" : f"{psutil.cpu_percent(interval=1)}%",
        "Memory Usage" : f"{psutil.virtual_memory().percent}%",
        "Disk Usage" : f"{psutil.disk_usage('/').percent}%"
    }
    return info
def get_resource_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return cpu , memory

def get_disk_health():
    import subprocess

    try:
        result = subprocess.run(
            ["diskutil", "info", "disk0"],
            capture_output=True,
            text=True,
            check=True
        )

        for line in result.stdout.splitlines():
            if "SMART Status" in line:
                return line.split(":")[-1].strip()

        return "Unavailable"

    except subprocess.SubprocessError:
        return "Unavailable"
