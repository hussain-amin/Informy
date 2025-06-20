import requests
import logging

def run(target):
    try:
        url = f"https://{target}" if not target.startswith("http") else target
        api_url = f"http://localhost:3000/extract?url={url}"
        logging.info(f"Querying Wappalyzer API for {url}")

        response = requests.get(api_url)
        if response.status_code != 200:
            logging.error(f"Wappalyzer API returned status code: {response.status_code}")
            return "Technology detection failed."

        data = response.json()
        applications = data.get("applications", [])

        if not applications:
            logging.warning("No technologies detected.")
            return "No technologies detected."

        result = []
        for app in applications:
            name = app.get("name", "Unknown")
            version = app.get("version", "N/A")
            confidence = app.get("confidence", "N/A")
            result.append(f"- {name} (v{version}, confidence: {confidence}%)")

        output = "\n".join(result)
        print("\n[ Detected Technologies ]")
        print(output)
        return output

    except Exception as e:
        logging.error(f"Error in tech detection: {e}")
        return "Technology detection failed due to an error."
