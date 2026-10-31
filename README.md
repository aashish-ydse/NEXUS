# NEXUS
# NEXUS — System Resource Monitor

**NEXUS** is a Python-based system monitoring tool that tracks CPU, RAM, and disk usage, stores resource readings in an SQLite database, and visualizes system performance through graphical charts.

Built as a practical Python project to explore system monitoring, database management, data visualization, and modular programming.

## ✨ Features

- **CPU Monitoring:** Tracks CPU usage.
- **RAM Monitoring:** Tracks memory usage.
- **Disk Monitoring:** Tracks disk usage.
- **Disk Health Status:** Checks SSD SMART status on macOS.
- **Data Storage:** Saves system readings in an SQLite database.
- **Performance Visualization:** Displays CPU, RAM, and disk usage in separate graphs.
- **Historical Data:** Retrieves previously stored readings for visualization.

## 🛠️ Technologies Used

- Python
- psutil
- SQLite3
- Matplotlib
- macOS `diskutil`

## 📁 Project Structure

```text
NEXUS/
│
├── main.py
├── nexus.db
│
└── core/
    ├── __init__.py
    ├── database.py
    ├── system_info.py
    └── visualization.py
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aashish-ydse/NEXUS.git
```

### 2. Navigate to the project directory

```bash
cd NEXUS
```

### 3. Install dependencies

```bash
pip install psutil matplotlib
```

### 4. Run NEXUS

```bash
python3 main.py
```

## 📊 How It Works

1. Collects system resource information using Python.
2. Stores collected readings in an SQLite database.
3. Retrieves historical readings from the database.
4. Uses Matplotlib to generate performance graphs.
5. Checks SSD SMART status using macOS system utilities.

## 💻 Platform

Currently developed and tested on **macOS**.

The SMART health check uses macOS's `diskutil` utility and may not work on other operating systems.🥲


## 🔮 Future Improvements(if I can do it)

- Resource usage alerts
- Live graphical dashboard
- 7-day and 30-day performance analytics
- Exportable monitoring reports
- Improved error handling and testing

## 👨‍💻 Author

**Aashish**

