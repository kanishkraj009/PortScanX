import socket
import threading
from colorama import Fore, Style, init

# Initialize colorama
init()

# ASCII Banner
print(Fore.RED + Style.BRIGHT + """
██████╗ ██████╗ ███████╗██╗     ███████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██║     ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██████╔╝█████╗  ██║     █████╗  ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║  ██║
██╔═══╝ ██╔═══╝ ██╔══╝  ██║     ██╔══╝  ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║  ██║
██║     ██║     ███████╗███████╗██║     ╚██████╔╝██║ ╚████║██║ ╚████║███████╗██████╔╝
╚═╝     ╚═╝     ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═════╝ 
       ⚠️  PRT Scanner: Vulnerability Enhanced Edition ⚠️
""" + Style.RESET_ALL)

# Mapping of ports to common services and known vulnerabilities
PORT_VULNERABILITIES = {
    21: ("FTP", "Check for anonymous login or outdated FTP server."),
    22: ("SSH", "Ensure strong passwords and avoid outdated SSH versions."),
    23: ("Telnet", "Telnet is insecure; consider replacing it with SSH."),
    25: ("SMTP", "Check for open relay configuration vulnerabilities."),
    53: ("DNS", "Verify DNS server configuration against cache poisoning."),
    80: ("HTTP", "Check for outdated web servers or missing patches."),
    110: ("POP3", "Ensure secure protocols like POP3S are used."),
    139: ("NetBIOS", "Ensure NetBIOS is secured against SMB vulnerabilities."),
    443: ("HTTPS", "Ensure SSL/TLS certificates are up-to-date."),
    3389: ("RDP", "Check for unauthorized access and apply security updates."),
}

def scan_port(ip_address, port):
    """
    Scans a single port on a given IP address and reports vulnerabilities.
    """
    try:
        socket.create_connection((ip_address, port), timeout=1)
        service = PORT_VULNERABILITIES.get(port, ("Unknown Service", "No known vulnerabilities."))
        print(Fore.GREEN + f"[+] Port {port} is OPEN on {ip_address}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"    Service: {service[0]}" + Style.RESET_ALL)
        print(Fore.RED + f"    Vulnerability Info: {service[1]}" + Style.RESET_ALL)
    except:
        pass  # Suppress output for closed ports


def scan(target, port_range):
    """
    Scans a range of ports on a target IP address using threading.
    """
    print(Fore.YELLOW + f"\n[*] Starting scan on {target} for ports {port_range[0]}-{port_range[1]}..." + Style.RESET_ALL)

    threads = []
    for port in range(port_range[0], port_range[1] + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete

    print(Fore.CYAN + f"[*] Scan completed for {target}" + Style.RESET_ALL)


def parse_ports(port_input):
    """
    Parses port input and returns a tuple representing the range of ports to scan.
    """
    if '-' in port_input:
        start, end = map(int, port_input.split('-'))
        if start > 0 and end > start:
            return (start, end)
    return (1, int(port_input))  # Default to scanning from port 1 to the specified number


# Main Execution
if __name__ == "__main__":
    targets = input("[*] Enter Targets to Scan (comma-separated): ")
    ports_input = input("[*] Enter Ports to Scan (e.g., 80 or 1-1000): ")

    try:
        port_range = parse_ports(ports_input)
    except ValueError:
        print(Fore.RED + "[!] Invalid port range. Exiting..." + Style.RESET_ALL)
        exit()

    if ',' in targets:
        print(Fore.MAGENTA + "[*] Scanning Multiple Targets..." + Style.RESET_ALL)
        for target in targets.split(','):
            scan(target.strip(), port_range)
    else:
        scan(targets.strip(), port_range)
