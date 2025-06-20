import argparse
import logging
from utils import setup_logging, save_report

def main():
    parser = argparse.ArgumentParser(description="Informy - Modular Recon CLI Tool")
    parser.add_argument("--whois", help="Perform WHOIS lookup", action="store_true")
    parser.add_argument("--dns", help="Enumerate DNS records", action="store_true")
    parser.add_argument("--subdomains", help="Enumerate subdomains", action="store_true")
    parser.add_argument("--portscan", help="Perform port scan", action="store_true")
    parser.add_argument("--banner", help="Grab banners from open ports", action="store_true")
    parser.add_argument("--tech", help="Detect web technologies", action="store_true")
    parser.add_argument("--target", help="Target domain or IP", required=True)
    parser.add_argument("--verbose", help="Verbose logging", action="store_true")

    args = parser.parse_args()
    setup_logging(verbose=args.verbose)

    logging.info("Informy started...")

    report_sections = {}

    try:
        if args.whois:
            from modules import whois_lookup
            report_sections["WHOIS Information"] = whois_lookup.run(args.target)

        if args.dns:
            from modules import dns_enum
            report_sections["DNS Records"] = dns_enum.run(args.target)

        if args.subdomains:
            from modules import subdomain_enum
            report_sections["Subdomains"] = subdomain_enum.run(args.target)

        if args.portscan:
            from modules import port_scan
            report_sections["Open Ports"] = port_scan.run(args.target)

        if args.banner:
            from modules import banner_grab
            report_sections["Banners"] = banner_grab.run(args.target)

        if args.tech:
            from modules import tech_detect
            report_sections["Technologies"] = tech_detect.run(args.target)

        if report_sections:
            report_path = save_report(args.target, report_sections)
            print(f"\n[+] Report saved to: {report_path}")

    except ImportError as e:
        logging.error(f"Module import failed: {e}")
    except Exception as e:
        logging.error(f"Runtime error: {e}")

    logging.info("Informy finished execution.")

if __name__ == "__main__":
    main()
