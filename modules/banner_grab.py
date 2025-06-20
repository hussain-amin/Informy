import socket
import logging

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))

        # Send a simple request for HTTP/HTTPS-like ports
        if port in [80, 8080, 443, 8443]:
            sock.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        return banner
    except Exception as e:
        logging.debug(f"Error grabbing banner from port {port}: {e}")
        return None

def run(target):
    logging.info(f"Performing banner grabbing on common ports for {target}")
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        logging.error(f"Could not resolve {target}")
        return "[ Banners ]\n- Could not resolve target.\n"

    ports_to_check = [21, 22, 25, 80, 110, 143, 443, 3306, 8080]
    output = "\n[ Banners ]\n"

    for port in ports_to_check:
        banner = grab_banner(ip, port)
        if banner:
            line = f"- Port {port}: {banner}\n"
            print(line.strip())
            output += line
        else:
            logging.debug(f"No banner on port {port}")

    if output.strip() == "[ Banners ]":
        output += "- No banners retrieved.\n"

    return output
