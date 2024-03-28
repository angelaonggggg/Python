import socket

def load_config(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if not line.startswith('#') and line.strip()]
        config = {
            'local_ip': lines[0],
            'local_port': int(lines[1]),
            'remote_ip': lines[2],
            'remote_port': int(lines[3])
        }
    return config

def run_server(local_ip, local_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((local_ip, local_port))
    print("Server is listening. Waiting for client to connect.")
    print("Connection established\n")

    while True:
        data, address = s.recvfrom(4096)
        print("\n==========================================\n")
        print("Client sent a message...")
        print(f"Message: {data.decode('utf-8')}")
        print("\n==========================================\n")
        message = input("Enter a message: ")
        print(f"Message sent: {message}")
        s.sendto(message.encode('utf-8'), address)

def run_client(remote_ip, remote_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        print("\n==========================================\n")
        message = input("Enter a message: ")
        print(f"Message sent: {message}")
        print("\n==========================================\n")
        s.sendto(message.encode('utf-8'), (remote_ip, remote_port))
        data, address = s.recvfrom(4096)
        print("Server sent a message...")
        print(f"Message: {data.decode('utf-8')}")

def main():
    while True: 
        config_file = input("Enter the filename: ")
        try: 
            config = load_config(config_file)
            break
        except FileNotFoundError:
            print("File not found.")

    if config['local_port'] == 1111:  
        run_server(config['local_ip'], config['local_port'])
    elif config['local_port'] == 5555: 
        run_client(config['remote_ip'], config['remote_port'])
    else:
        print("Invalid configuration.")

if __name__ == "__main__":
    main()
