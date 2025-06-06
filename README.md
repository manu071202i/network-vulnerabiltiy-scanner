# Network Vulnerability Scanner

## Overview  
The **Network Vulnerability Scanner** is a simple Python-based tool to scan your network for open common ports that could indicate potential vulnerabilities.

## Features  
- Scans a target IP network range for common open ports (SSH, HTTP, HTTPS, FTP, RDP, SMTP).  
- Lists hosts with open ports for prioritization and further analysis.  

## Goals  
- Identify exposed network services that may require patching or additional protection.  
- Help network administrators quickly assess basic security gaps.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-vulnerability-scanner.git
   cd network-vulnerability-scanner
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies (none required currently):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scanner by specifying the target network in CIDR notation:

```bash
python scanner.py --target 192.168.1.0/24
```

Example output:

```
Scanning network: 192.168.1.0/24
[!] 192.168.1.5 has open ports:
    - Port 22 (SSH)
    - Port 80 (HTTP)
Scan complete.
```

## Contributing  
Feel free to fork the repository and submit pull requests to add more features, improve scanning speed, or integrate with patch management.

## License  
MIT License

---