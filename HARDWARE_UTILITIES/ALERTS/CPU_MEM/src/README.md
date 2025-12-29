Import libraries: Bring in psutil for system stats and requests for sending alerts.

Set thresholds: Define numeric limits for CPU usage (e.g., 80%) and memory usage (e.g., 75%).

Check resources:

Use psutil.cpu_percent() to get current CPU usage.

Use psutil.virtual_memory().percent to get current memory usage.

Compare to thresholds:

If CPU usage exceeds its threshold, trigger an alert.

If memory usage exceeds its threshold, trigger an alert.

Send alert: Use requests.post() to hit a webhook with a message describing which threshold was exceeded.

Loop (optional): Repeat the check every N seconds using time.sleep(N) to continuously monitor.

Optional enhancements:

Include both CPU and memory in a single alert.

Customize the message format.

Make thresholds configurable via a simple config file.