import paramiko

ip = "192.168.1.104"
user = "guest"
passwd = "Jayathi$6S"

# Connect to the SSH server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip, username=user, password=passwd)

# Execute a command remotely
stdin, stdout, stderr = ssh.exec_command("python3 -c 'print([x**2 for x in range(10)])'")

# Read & decode the output
output = stdout.read().decode('utf-8')
error = stderr.read().decode('utf-8')

# Print the output
print(output)
print(error)

# Close the SSH connection
ssh.close()

