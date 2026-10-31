import os
import time
from core.system_info import get_system_info , get_disk_health
from core.database import initialize_database , save_reading


def show_dashnoard():

    initialize_database()

    while True:

        info = get_system_info()
        disk_health = get_disk_health()

        cpu = float(info["CPU Usage"].replace("%"," "))
        memory = float(info["Memory Usage"].replace("%", " "))
        disk = float(info["Disk Usage"].replace("%", " "))
        save_reading(cpu,memory,disk)
        os.system("clear")

        print("="*42)
        print("           N E X U S")
        print("     PARSONAL SYSTEM MONITOR")
        print("="*42)

        for key,value in info.items():
            print(f"    {key:<15} : {value}")
        print(f"  {'  Disk Health':<15} : {disk_health}")
        print("="*42)
        print("  Logging : Active")
        print(" Database : Connected")
        print(" Refrashing : 2 seconds...")
        print(" Press CTRL + C to exit")
        time.sleep(2)
if __name__ == "__main__":
        try:
            show_dashnoard()
        except KeyboardInterrupt:
            print("\nNEXUS stopped")
            
