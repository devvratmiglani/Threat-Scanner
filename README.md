# Threat Scanner

## Overview
This project scans different IP addresses and files to determine whether they are malicious or not. It leverages the VirusTotal API to fetch detailed threat intelligence and provide a risk assessment for given inputs.

## Features
- Scan IP addresses for potential threats.
- Scan files to check for malware.
- Utilize VirusTotal API for scanning and reporting.
- Log and display results in a user-friendly format.

## Installation
### Prerequisites
Ensure you have Python installed on your system.

```sh
python --version
```
If Python is not installed, download and install it from [Python Official Site](https://www.python.org/).

### Clone the Repository
```sh
git clone https://github.com/devvratmiglani/Threat-Scanner.git
cd Threat-Scanner
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Configuration
1. Get an API key from [VirusTotal](https://www.virustotal.com/gui/join-us).
2. Open `settings.py` and add your API key:
   ```python
   API_KEY = "your_virustotal_api_key"
   ```

## Usage
### Scan a File
Run the following command to scan a file:
```sh
python single_file.py /path/to/file
```

### Scan an IP Address
Run the following command to scan an IP:
```sh
python single_ip.py 192.168.1.1
```

## File Structure
```
.
├── single_file.py    # Script to scan files
├── single_ip.py      # Script to scan IPs
├── settings.py       # Configuration file for API keys
├── vt.py             # Core logic for interacting with VirusTotal API
├── .gitignore        # Files to ignore in git
├── LICENSE           # License information
├── README.md         # Documentation file
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements.


