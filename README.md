<p align="center"> <img src="Informy-logo.png" width="180" alt="Informy Logo"> </p>


🔍 Informy – Modular Reconnaissance Tool
Informy is a modular command-line based reconnaissance tool designed to
perform basic yet crucial information gathering tasks for cybersecurity assessments.

Developed as part of a cybersecurity internship at ITSOLERA.

🚀 Features
✅ WHOIS Lookup
✅ DNS Enumeration (A, MX, TXT, NS)
✅ Subdomain Enumeration (via crt.sh)
✅ Port Scanning (common ports)
✅ Banner Grabbing
✅ Technology Detection (via Docker-based Wappalyzer API)
✅ Modular design with CLI flags
✅ Verbose logging and .txt based reporting with timestamps

💠 Installation
🔧 Requirements
Python 3.8+
pip
Docker (required for Technology Detection module)

📦 Clone and Install
git clone https://github.com/hussain-amin/Informy.git
cd Informy
pip install -r requirements.txt

🐳 Docker Setup (for Technology Detection)
Informy uses a Docker-based Wappalyzer API for technology detection.

Step 1: Run Wappalyzer API in Docker
docker run -p 3000:3000 hunterio/wappalyzer-api
(Keep this container running while using the --tech flag.)

💻 Usage
python main.py --target <domain> [options]

Options:
Flag	        Description
--whois	        Perform WHOIS lookup
--dns	        DNS Enumeration
--subdomains	Subdomain enumeration
--portscan	    Port scanning
--banner	    Banner grabbing
--tech	        Technology detection (requires Docker)
--verbose	    Enable verbose (debug) logging

Example:
python main.py --target github.com --dns --whois --verbose

📄 Output Reports
Reports are saved inside the reports/ folder

Format: .txt, timestamped

Includes IP resolutions and clean section-wise output for documentation

📁 Project Structure
Informy/
├── modules/
│ ├── whois_lookup.py
│ ├── dns_enum.py
│ ├── subdomain_enum.py
│ ├── port_scan.py
│ ├── banner_grab.py
│ └── tech_detect.py
├── reports/
│ └── *.txt
├── main.py
├── utils.py
├── requirements.txt
├── README.md
└── Informy-logo.png

🐳 Running Informy with Docker (Optional)
You can run the tool itself inside Docker (without needing to install Python locally).

Step 1: Build the Docker image
docker build -t informy .

Step 2: Run Informy inside Docker
docker run --rm informy --target github.com --dns --whois

Save Reports to Host
Windows:
docker run --rm -v %cd%/reports:/app/reports informy --target github.com --dns --whois

Linux/macOS:
docker run --rm -v $(pwd)/reports:/app/reports informy --target github.com --dns --whois

📌 Disclaimer
This project is not licensed for public distribution.
Intended strictly for educational and internship evaluation purposes.

✍️ Author
Hussain Amin Manj
Developed during internship at ITSOLERA

