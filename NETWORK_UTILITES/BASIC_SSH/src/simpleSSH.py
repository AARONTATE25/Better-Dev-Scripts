import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
with open("clients.txt", "r") as f:

    for lines in f:
        line = lines.split(",")

        # Note; There is usually an error with the username or password
        # if I don't strip the whitespace one at a time

        hostname = (line[0])
        username = (line[1].strip())
        password = (line[2].strip())

        client.connect(hostname= hostname, username= username, password=password)

        #stdin,stdout,stderr - client.exec_command("COMMAND")
        stdin, stdout, stderr = client.exec_command("ping -c 3 google.com")
# The following line blocks do the same thing

    # this method print outputs in realtime
    for line in stdout:
        print(line)
    for line in stdout:
        print(line)
    for line in stderr:
        print(line)


    # this block prints the output after the commands have executed.
    print(stdout.read().decode())
    print(stderr.read().decode())
#   Dont forget to close your client

    client.close()
