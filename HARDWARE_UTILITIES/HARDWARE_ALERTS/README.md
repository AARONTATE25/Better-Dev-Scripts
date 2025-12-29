# CPU and Memory Monitoring Script Instructions

## Goal
Monitor system CPU and memory usage and send an alert if thresholds are exceeded.

## Libraries
- `psutil` — for checking CPU and memory usage.
- `requests` — for sending alerts via webhook.

## Steps

1. **Import Libraries**  
   Import `psutil` and `requests`.

2. **Set Thresholds**  
   Define numeric limits for CPU and memory usage (e.g., CPU > 80%, Memory > 75%).

3. **Check Resources**  
   - Use `psutil.cpu_percent()` to get the current CPU usage.  
   - Use `psutil.virtual_memory().percent` to get current memory usage.

4. **Compare to Thresholds**  
   - If CPU usage exceeds its threshold, trigger an alert.  
   - If memory usage exceeds its threshold, trigger an alert.

5. **Send Alert**  
   Use `requests.post()` to hit a webhook with a message describing which threshold was exceeded.

6. **Loop (Optional)**  
   Repeat the check every N seconds using `time.sleep(N)` to continuously monitor.

7. **Optional Enhancements**  
   - Include both CPU and memory in a single alert.  
   - Customize the message format.  
   - Make thresholds configurable via a simple config file.
# Example Output

### Scenario 1: CPU exceeds threshold
```

ALERT: CPU usage high!
Current CPU Usage: 87%
Memory Usage: 62%

```

### Scenario 2: Memory exceeds threshold
```

ALERT: Memory usage high!
Current CPU Usage: 45%
Memory Usage: 79%

```

### Scenario 3: Both exceed thresholds
```

ALERT: CPU and Memory usage high!
Current CPU Usage: 92%
Memory Usage: 81%

```

### Scenario 4: Normal usage (no alert)
```

CPU Usage: 35%
Memory Usage: 48%
Status: All systems normal.
