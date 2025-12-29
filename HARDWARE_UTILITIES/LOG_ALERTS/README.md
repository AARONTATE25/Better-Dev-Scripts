# System Health Monitoring Script

## Overview
This Python script monitors the system's **CPU, memory, and disk usage** and logs the metrics into a file named `health.log`. It provides warnings if any resource exceeds the defined thresholds. The script runs in a continuous loop and checks the system at regular intervals.

---

## Libraries Used
1. **psutil** — To gather system resource metrics (CPU, memory, disk usage).  
2. **logging** — To log system health information into a file.  
3. **time** — To control the monitoring interval between checks.

---

## Configuration

- **CPU_THRESHOLD**: Maximum CPU usage percentage before a warning is logged (default: 2%).  
- **MEMORY_THRESHOLD**: Maximum RAM usage percentage before a warning is logged (default: 50%).  
- **DISK_THRESHOLD**: Maximum disk usage percentage before a warning is logged (default: 90%).  
- **CHECK_INTERVAL**: Time in seconds between consecutive checks (default: 50 seconds).  

You can modify these constants at the top of the script according to your system and monitoring needs.

---

## Functions

1. **check_cpu()**  
   - Measures CPU usage using `psutil.cpu_percent(interval=1)`.  
   - Returns a warning message if CPU usage exceeds `CPU_THRESHOLD`, otherwise logs normal usage.

2. **check_memory()**  
   - Measures memory usage using `psutil.virtual_memory()`.  
   - Returns a warning message if memory usage exceeds `MEMORY_THRESHOLD`, otherwise logs normal usage.

3. **check_disk(path)**  
   - Measures disk usage for a given path using `psutil.disk_usage(path)`.  
   - Returns a warning message if disk usage exceeds `DISK_THRESHOLD`, otherwise logs normal usage.

4. **monitor_system()**  
   - Calls `check_cpu()`, `check_memory()`, and `check_disk("/")`.  
   - Logs the output of each check into `health.log`.

---

## How It Works

1. The script starts by configuring the logging system to write messages to `health.log`.  
2. It continuously monitors CPU, memory, and disk usage.  
3. For each resource, it compares the current usage to the defined thresholds.  
4. If a threshold is exceeded, a warning message is logged. Otherwise, normal usage is logged.  
5. After logging, the script waits for `CHECK_INTERVAL` seconds before checking again.  

---

## Example Log Output
    
    [2025-12-29 05:00:01] CPU USAGE: 1.5
    [2025-12-29 05:00:01] MEMORY USAGE: 45.2
    [2025-12-29 05:00:01] DISK USAGE: 70.3
    [2025-12-29 05:00:51] WARNING: HIGH CPU USAGE 87.0
    [2025-12-29 05:00:51] MEMORY USAGE: 47.8
    [2025-12-29 05:00:51] DISK USAGE: 71.0
    [2025-12-29 05:01:41] CPU USAGE: 2.0
    [2025-12-29 05:01:41] WARNING: HIGH MEMORY USAGE 52.5
    [2025-12-29 05:01:41] DISK USAGE: 72.1


---

## Notes
- The CPU threshold is set extremely low (2%) for demonstration purposes; adjust as needed.  
- The disk check monitors the root directory `/`, but this can be changed to any mount path.  
- The script runs indefinitely until manually stopped.

## Potential Improvements

- **Reduce CPU Overhead**: Instead of using `psutil.cpu_percent(interval=1)` in every loop, consider measuring CPU asynchronously or using a shorter interval to reduce the script’s own CPU impact.  

- **Configurable Parameters**: Move thresholds and check intervals to a configuration file or environment variables so changes can be made without modifying the code.  

- **Alerting System**: Integrate real-time alerts (e.g., email, Slack, or webhook) so critical warnings are notified immediately instead of only logging to a file.

- **Graceful Shutdown**: Handle `KeyboardInterrupt` exceptions to allow the script to exit cleanly and ensure logs are properly flushed when the user stops the program with Ctrl+C.
