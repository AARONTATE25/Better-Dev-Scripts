import psutil
import logging
import time


logging.basicConfig(filename='docs/health.log', level=logging.INFO,
                    format='[%(asctime)s] %(message)s')


CPU_THRESHOLD = 2     # percent
MEMORY_THRESHOLD = 50    # percent
DISK_THRESHOLD = 90      # percent
CHECK_INTERVAL = 50     # seconds, optional

def check_cpu():
    # Measure CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    # Return True if above threshold
    if cpu_usage > CPU_THRESHOLD:
        return f"WARNING: HIGH CPU USAGE {cpu_usage}"
    else:
        return f"CPU USAGE: {cpu_usage}"

def check_memory():
    # Measure memory usage RAM
    mem_usage = psutil.virtual_memory()
    # Return True if above threshold
    if mem_usage.percent > MEMORY_THRESHOLD:
        return f"WARNING: HIGH MEMEORY USAGE {mem_usage.percent}"
    else:
        return f"MEMORY USAGE: {mem_usage.percent}"

def check_disk(path):
    # Measure disk usage at given path
    disk_usage = psutil.disk_usage(path)
    # Return True if above threshold
    if disk_usage.percent > DISK_THRESHOLD:
        return f"WARNING: HIGH DISK USAGE {disk_usage.percent}"
    else:
        return f"DISK USAGE: {disk_usage.percent}"

def monitor_system():
    # Call check_cpu(), check_memory(), check_disk()
    cpu_stat = check_cpu()
    mem_stat = check_memory()
    disk_stat = check_disk("/")

    # Log all metrics
    logging.info(cpu_stat)
    logging.info(mem_stat)
    logging.info(disk_stat)


while True:
    monitor_system()
    time.sleep(CHECK_INTERVAL)
