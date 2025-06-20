import dns.resolver
import logging

def query_dns(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        logging.warning(f"No {record_type} record found for {domain}")
    except dns.resolver.NXDOMAIN:
        logging.error(f"Domain {domain} does not exist.")
    except Exception as e:
        logging.error(f"Error querying {record_type} record: {e}")
    return []

def run(target):
    logging.info(f"Performing DNS Enumeration for {target}")

    record_types = ["A", "MX", "TXT", "NS"]
    output = "[ DNS Records ]\n"

    for rtype in record_types:
        records = query_dns(target, rtype)
        output += f"\n[ {rtype} Records ]\n"
        if records:
            for record in records:
                output += f"- {record}\n"
        else:
            output += "- No records found or query failed.\n"

    return output
