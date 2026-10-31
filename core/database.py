import sqlite3
def initialize_database():
    connection = sqlite3.connect("nexus.db")
    cursor = connection.execute("PRAGMA table_info(system_logs)")
    columns = [column[1] for column in cursor.fetchall()]
    if "disk_usage" not in columns :
        connection.execute("ALTER TABLE system_logs ADD COLUMN disk_usage REAL")
    connection.execute("""CREATE TABLE IF NOT EXISTS System_logs (id INTEGER PRIMARY KEY AUTOINCREMENT , timetamp DATETIME DEFAULT CURRENT_TIMESTAMP , cpu_usage REAL, memory_usage REAL , disk_usage REAL)""")
    connection.commit()
    connection.close()


def save_reading(cpu_usage, memory_usage , disk_usage):
    connection = sqlite3.connect("nexus.db")
    connection.execute("""INSERT INTO system_logs (cpu_usage,memory_usage, disk_usage) VALUES (?,?,?)""" , (cpu_usage , memory_usage , disk_usage))
    connection.commit()
    connection.close()

def get_reading_history():
    connection = sqlite3.connect("nexus.db")
    cursor = connection.execute("""SELECT id , timetamp , cpu_usage , memory_usage, disk_usage FROM system_logs ORDER BY id DESC LIMIT 10""")
    reading = cursor.fetchall()
    connection.close()
    return reading

if __name__ == "__main__":
    initialize_database()
    from system_info import get_resource_usage
    cpu , memory = get_resource_usage()
    save_reading(cpu , memory)
    print(f"CPU saved : {cpu}%")
    print(f"Memmory saved : {memory}%")
    history = get_reading_history()
    print("\n--- NEXUS READING HISTORY ---")
    for reading in history:
        print(reading)
    