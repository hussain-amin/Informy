import logging
import os
import datetime
import re

def setup_logging(verbose=False):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

def sanitize_filename(text):
    return re.sub(r'[^\w\-_.]', '_', text)

def save_report(target, sections, output_dir="reports"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_target = sanitize_filename(target)
    filename = f"{safe_target}_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"{'='*60}\n")
            f.write(f"Recon Report for {target}\n")
            f.write(f"Generated: {timestamp}\n")
            f.write(f"{'='*60}\n\n")

            for section_title, content in sections.items():
                f.write(f"{section_title.center(60, '-')}\n")
                f.write(content.strip() + "\n\n")

        logging.info(f"Report saved to: {filepath}")
        return filepath

    except Exception as e:
        logging.error(f"Failed to save report: {e}")
        return None

# Optional: for HTML reports later
# def save_html_report(target, sections, output_dir="reports"):
#     ...
