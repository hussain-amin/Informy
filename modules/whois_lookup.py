import whois
import logging

def run(target):
    try:
        logging.info(f"Performing WHOIS lookup for {target}")
        domain_info = whois.whois(target)

        report = "[ WHOIS Information ]\n"
        for key, value in domain_info.items():
            report += f"{key}: {value}\n"

        return report

    except Exception as e:
        logging.error(f"WHOIS lookup failed: {e}")
        return f"[ WHOIS Information ]\nWHOIS lookup failed: {e}\n"
