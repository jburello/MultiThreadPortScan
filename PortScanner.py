import socket
import threading
from queue import Queue

queue = Queue()
lock = threading.Lock()

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def portscan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the socket connection
        sock.connect((target, port))
        sock.close()
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker(target, open_ports):
    while not queue.empty():
        port = queue.get()
        if portscan(target, port):
            with lock:
                open_ports.append(port)
            print(f"Port {port} is open on {target}.")
        queue.task_done()

def get_port_range():
    while True:
        port_range = input("Enter port range to scan (e.g., 1-1024): ").strip()
        if '-' not in port_range:
            print("Please enter the range in the format start-end, e.g., 1-1024")
            continue
        try:
            start, end = map(int, port_range.split('-'))
            if not (1 <= start <= 65535 and 1 <= end <= 65535):
                print("Ports must be between 1 and 65535.")
                continue
            if start > end:
                print("Start port must be less than or equal to end port.")
                continue
            return range(start, end + 1)
        except ValueError:
            print("Invalid input. Ports must be numbers.")

def main():
    while True:
        target = input("Enter an IP address or hostname to scan (or type 'exit' to quit): ").strip()
        if target.lower() == "exit":
            print("Exiting port scanner. Goodbye!")
            break
        if not target:
            print("Input cannot be empty. Please enter a valid IP or hostname.")
            continue

        # Resolve IP if hostname
        if not is_valid_ip(target):
            try:
                target = socket.gethostbyname(target)
            except socket.gaierror:
                print("Invalid hostname or IP. Please try again.")
                continue

        port_list = get_port_range()

        # Clear previous results
        open_ports = []

        fill_queue(port_list)

        thread_list = []
        num_threads = 100  # Number of threads to use
        for _ in range(num_threads):
            thread = threading.Thread(target=worker, args=(target, open_ports))
            thread.daemon = True  # Allows program to exit even if threads are alive
            thread.start()
            thread_list.append(thread)

        queue.join()  # Wait for all ports to be scanned

        print("\nPort scan complete.")
        print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    main()