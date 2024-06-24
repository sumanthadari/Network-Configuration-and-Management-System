import psutil

def monitor_network():
    try:
        # Get network interfaces and addresses
        interfaces = psutil.net_if_addrs()
        for interface_name, interface_addresses in interfaces.items():
            print(f"Interface: {interface_name}")
            for address in interface_addresses:
                print(f"  Address: {address.address}")

        # Get network connections
        connections = psutil.net_connections()
        for conn in connections:
            print(f"Connection: {conn}")

    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
monitor_network()
