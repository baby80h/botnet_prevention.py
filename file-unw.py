import os
import sys
import time
import socket
import threading
import requests
import ipaddress

# GitHub API endpoint
GITHUB_API_ENDPOINT = "https://api.github.com/meta"

# Function to get the current IP address of the system
def get_current_ip():
    response = requests.get(GITHUB_API_ENDPOINT)
    return response.json()["hooks"][0]

# Function to check if an IP address is in the GitHub IP range
def is_ip_in_github_range(ip_address):
    response = requests.get(GITHUB_API_ENDPOINT)
    github_ips = response.json()["hooks"]
    for ip_range in github_ips:
        if ipaddress.ip_address(ip_address) in ipaddress.ip_network(ip_range):
            return True
    return False

# Function to start a port scan
def start_port_scan(target_ip, port_range):
    print(f"Scanning {target_ip} for open ports...")
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Function to block an IP address using iptables
def block_ip(ip_address):
    os.system(f"iptables -A INPUT -s {ip_address} -j DROP")
    print(f"Blocked IP address: {ip_address}")

# Function to handle incoming connections
def handle_connection(conn, addr):
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received data from {addr}: {data}")
        if "scan" in data:
            start_port_scan(addr[0], (1, 1024))
        elif "block" in data:
            block_ip(addr[0])
        else:
            conn.send("Invalid command".encode())
    conn.close()

# Function to start the server
def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Server started on port {port}")
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()

# Main function
def main():
    current_ip = get_current_ip()
    print(f"Current IP address: {current_ip}")
    if is_ip_in_github_range(current_ip):
        print("Your IP address is in the GitHub IP range.")
    else:
        print("Your IP address is not in the GitHub IP range.")
        sys.exit(1)

    port = int(input("Enter the port number to start the server: "))
    start_server(port)

if __name__ == "__main__":
    main()