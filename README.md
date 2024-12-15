# PortScanX: Vulnerability Scanner for Network Services

PortScanX is a Python-based port scanner designed to detect vulnerabilities associated with commonly used network services. It checks for open ports on a target machine and reports potential security risks related to those services.

## Features
- Scans ports in a specified range (single or multiple).
- Identifies known vulnerabilities associated with common services such as FTP, SSH, HTTP, and more.
- Multi-threaded scanning for faster performance.
- Customizable port range and target IP addresses.
- Easy-to-read output with color-coded information using the `colorama` library.

## Supported Ports and Vulnerabilities
PortScanX checks the following ports for known vulnerabilities:
- **Port 21 (FTP)**: Checks for anonymous login or outdated FTP servers.
- **Port 22 (SSH)**: Ensures strong passwords and avoids outdated SSH versions.
- **Port 23 (Telnet)**: Recommends replacing Telnet with SSH due to security concerns.
- **Port 25 (SMTP)**: Checks for open relay configurations.
- **Port 53 (DNS)**: Verifies DNS server configuration to avoid cache poisoning.
- **Port 80 (HTTP)**: Identifies outdated web servers or missing patches.
- **Port 110 (POP3)**: Recommends using secure protocols like POP3S.
- **Port 139 (NetBIOS)**: Checks for security vulnerabilities related to SMB.
- **Port 443 (HTTPS)**: Verifies SSL/TLS certificate validity.
- **Port 3389 (RDP)**: Ensures RDP is properly secured against unauthorized access.

## Installation
To use PortScanX, you need Python 3 and the `colorama` library for colored output. You can install `colorama` using `pip`:

pip install colorama


Clone or download the repository to your local machine:
git clone https://github.com/yourusername/PortScanX.git
cd PortScanX

Run the script:
python scanner.py
