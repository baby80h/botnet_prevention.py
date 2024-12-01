Network Security Utility
This project is a Python-based utility for monitoring and managing network security. It provides functionalities like port scanning, IP address validation against GitHub's ranges, and blocking specific IPs using iptables. It also includes a server component to handle incoming connections and perform specific tasks based on commands received.

Features
GitHub IP Range Validation: Verifies if the system's current IP is part of GitHub's hooks IP ranges using the GitHub API.
Port Scanning: Scans a given target IP within a specified port range to identify open ports.
IP Blocking: Blocks specified IP addresses using iptables.
Multithreaded Server: Listens for incoming connections and executes commands like port scanning or IP blocking based on client input.
Project Structure
file-unw.py: The main script containing all the functionality, including:
API interaction with GitHub.
Port scanning logic.
IP blocking mechanism.
Server setup for handling client requests.
Requirements
Python 3.8 or higher
Required Python libraries:
requests
ipaddress
Installation
Clone the repository:
bash
Copy code
git clone <repository-url>
cd <repository-directory>
Install the dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Run the Script
Start the script:

bash
Copy code
python file-unw.py
Features
Check Current IP Address: The script fetches the system's current IP and checks if it belongs to GitHub's hooks IP ranges.

Start the Server: After validating the IP, start the server on a specified port to handle incoming connections and perform tasks like:

Scanning open ports.
Blocking IP addresses.
Configuration
The server listens on all interfaces (0.0.0.0) by default.
IP address validation uses the GitHub API endpoint: https://api.github.com/meta.
License
This project is licensed under the MIT License.

Replace <repository-url> with the actual URL of your GitHub repository. This README provides an overview and instructions for users to understand and use your project.
