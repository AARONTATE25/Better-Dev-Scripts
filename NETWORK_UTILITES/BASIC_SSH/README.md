# SSH Automation Script Overview

## Paramiko Components Used

- **`paramiko.SSHClient`**  
  This is the core object used to establish SSH connections. It handles the encrypted session, authentication, and communication with the remote host.

- **`load_system_host_keys()`**  
  Loads known host keys from the local system. This allows the client to trust previously known servers and helps prevent man-in-the-middle attacks.

- **`connect()`**  
  Opens an SSH connection to the remote host using the provided hostname, username, and password. This method performs authentication and starts the secure session.

- **`exec_command()`**  
  Executes a shell command on the remote machine. It returns three file-like objects:
  - `stdin` for sending input to the command
  - `stdout` for reading normal command output
  - `stderr` for reading error messages

---

## What the Code Does

- Reads a list of remote systems and credentials from `clients.txt`.
- Connects to each system over SSH using Paramiko.
- Executes a network test command (`ping -c 3 google.com`) on the remote host.
- Displays both standard output and error output from the command execution.
- Closes the SSH connection once the command finishes.

---

## Why This Is Useful

- Automates repetitive SSH tasks across multiple machines.
- Allows centralized validation of connectivity or system behavior.
- Serves as a foundation for more advanced remote administration scripts.
