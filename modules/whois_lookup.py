import whois
import logging

def run(target):
    try:
        logging.info(f"Performing WHOIS lookup for {target}")
        domain_info = whois.whois(target)

        output = "\n[ WHOIS Information ]\n"
        for key, value in domain_info.items():
            output += f"{key}: {value}\n"

        print(output)  # still show to user
        return output  # return to main
    except Exception as e:
        logging.error(f"WHOIS lookup failed: {e}")
        return "[ WHOIS Information ]\nWHOIS lookup failed.\n"
