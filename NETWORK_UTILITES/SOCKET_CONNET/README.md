## Network Connectivity Monitoring Script Instructions
# Goal
Check if the system can reach a list of important servers and send an alert if any server is unreachable.

# Libraries
1. `socket` — for checking connectivity to a server and port.  
2. `requests` — for sending alerts via webhook.

# Steps

1. **Import Libraries**  
   Import `socket` and `requests`.

2. **Define Servers**  
   Create a list of servers with hostnames/IPs and ports to check.

3. **Check Connectivity**  
   - Attempt to create a socket connection to each server.  
   - Set a timeout (e.g., 5 seconds) for the connection attempt.  
   - Record which servers are reachable and which are not.

4. **Send Alert**  
   - If any server is unreachable, use `requests.post()` to send an alert describing the issue.  

5. **Loop (Optional)**  
   - Repeat the check every N seconds using `time.sleep(N)` to continuously monitor network status.

# Optional Enhancements
1. Include round-trip time or latency in the alert.  
2. Retry a few times before sending an alert.  
3. Make server list and timeout configurable via a config file.

# Example Outputs

**Scenario 1: One server down**  

    ALERT: Network connectivity issue detected!
    Unreachable servers: server2.example.com:443


**Scenario 2: Multiple servers down**  

    
    ALERT: Network connectivity issues detected!
    Unreachable servers: server1.example.com:22, server3.example.com:80


**Scenario 3: All servers reachable**  

    
    All servers reachable.
    Status: Network connectivity normal.