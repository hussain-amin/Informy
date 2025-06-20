import requests
import logging

def from_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    logging.info(f"Querying crt.sh for subdomains of {domain}")
    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            logging.error(f"crt.sh request failed with status {response.status_code}")
            return []

        data = response.json()
        subdomains = set()
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                if domain in sub:
                    subdomains.add(sub.strip())
        return sorted(subdomains)

    except Exception as e:
        logging.error(f"Error querying crt.sh: {e}")
        return []

def run(domain):
    logging.info(f"Starting subdomain enumeration for {domain}")
    subdomains = from_crtsh(domain)

    output = f"\n[ Subdomains Found via crt.sh ]\n"
    if subdomains:
        for sub in subdomains:
            output += f"- {sub}\n"
    else:
        output += "- No subdomains found.\n"

    print(output)
    return output
