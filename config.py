import paramiko
import time

def configure_router(hostname, username, password):
    try:
        # Connect to the router
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password, timeout=5)

        # Start an interactive shell session
        shell = ssh.invoke_shell()

        # Wait for the prompt
        time.sleep(2)
        shell.recv(65535).decode()

        # Send configuration commands
        shell.send("enable\n")
        shell.send("configure terminal\n")
        shell.send("interface GigabitEthernet0/0\n")
        shell.send("ip address 192.168.1.1 255.255.255.0\n")
        shell.send("no shutdown\n")
        shell.send("exit\n")
        shell.send("router ospf 1\n")
        shell.send("network 192.168.1.0 0.0.0.255 area 0\n")
        shell.send("end\n")

        # Wait for commands to be applied
        time.sleep(2)
        output = shell.recv(65535).decode()
        print(output)

        # Close SSH session
        ssh.close()

        print("Configuration completed successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
router_ip = '192.168.1.1'
username = 'admin'
password = 'password'

configure_router(router_ip, username, password)

