import socket
import logging

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    5900: "VNC",
    3389: "RDP"
}

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def run(target):
    logging.info(f"Starting port scan for {target}")
    output = "[ Open Ports ]\n"

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        logging.error(f"Could not resolve {target}")
        return output + "- Could not resolve domain.\n"

    found_open = False
    for port, service in COMMON_PORTS.items():
        if scan_port(ip, port):
            output += f"- Port {port} ({service}) is OPEN\n"
            found_open = True

    if not found_open:
        output += "- No common ports found open.\n"

    return output
