Service Uptime Monitoring Script Instructions
# Goal
Check if critical services are running on the system and send an alert if any service is down.

# Libraries
1. `subprocess` — for checking service status.  
2. `requests` — for sending alerts via webhook.

# Steps

1. **Import Libraries**  
   Import `subprocess` and `requests`.

2. **Define Services**  
   Create a list of services to monitor (e.g., `nginx`, `ssh`, `mysql`).

3. **Check Service Status**  
   - Use `subprocess.run()` to check each service’s status.  
   - Capture the output and determine if the service is active or inactive.

4. **Send Alert**  
   - If any service is inactive, use `requests.post()` to send an alert specifying which services are down.

5. **Loop (Optional)**  
   - Repeat the check every N seconds using `time.sleep(N)` to continuously monitor service uptime.

# Optional Enhancements
1. Include service restart attempt before sending an alert.  
2. Track uptime duration for each service.  
3. Make the service list and alert webhook configurable via a config file.

# Example Output

**Scenario 1: One service down**  

    ALERT: Service down detected!
    Inactive service: nginx


**Scenario 2: Multiple services down**  


    ALERT: Multiple services down!
    Inactive services: mysql, ssh


**Scenario 3: All services running**  


    All services are running.
    Status: System operational.