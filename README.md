# 🔍 PortScanner

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Purpose](https://img.shields.io/badge/Purpose-Educational-orange?style=for-the-badge)](https://github.com/ShehanSulakshana/PortScanner)

> ⚠️ **Disclaimer:** This tool is built strictly for **educational and authorized security testing purposes only**. Scanning targets without prior mutual consent is illegal. The author assumes no liability and is not responsible for any misuse or damage caused by this program.

---

## 📌 Overview

**PortScanner** is a lightweight, Python-based network reconnaissance tool designed to scan target hosts, discover active ports, and identify running services in real time. Built using core networking fundamentals, it serves as a practical project for learning how socket connections and network reconnaissance operate under the hood.

---

## ✨ Features

- **Hostname & IP Resolution:** Seamlessly accepts both raw IP addresses (e.g., `192.168.1.1`) and domain names (e.g., `scanme.nmap.org`).
- **Custom Port Range:** Target specific standard ranges (e.g., `1-1024`) or full scan ranges (`1-65535`).
- **Real-Time Stream:** Live terminal feedback as open ports are discovered.
- **Service Mapping:** Automatically resolves common standard port numbers to their associated protocols (e.g., HTTP, SSH, FTP, HTTPS).
- **Result Export:** Option to save scan results into a file for further analysis.

---

## 📁 Repository Structure

```text
PortScanner/
├── portscanner.py   # Main application script
├── req.txt          # Project dependencies
├── LICENSE          # MIT License
└── README.md        # Project documentation
```

---

## ⚙️ Quick Start

### Prerequisites

- Python 3.8 or higher installed on your system.

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShehanSulakshana/PortScanner.git
   cd PortScanner
   ```

2. **Install dependencies:**
   ```bash
   pip install -r req.txt
   ```

3. **Run the scanner:**
   ```bash
   python portscanner.py
   ```

---

## 🛡️ Cybersecurity Application

Understanding port scanning techniques is critical for several core cybersecurity domains:

- **Penetration Testing:** Initial discovery phase to map out an organization's exposed attack surface.
- **Network Administration:** Auditing internal and perimeter firewalls to prevent unauthorized external services from being exposed.
- **CTF & Lab Challenges:** Essential skill for host discovery in controlled hacking environments.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/ShehanSulakshana/PortScanner/issues) if you want to contribute.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more details.

---

## 👨‍💻 Author

**Shehan Sulakshana**  
Cybersecurity Undergraduate | Python & Network Security Enthusiast  
- **GitHub:** [@ShehanSulakshana](https://github.com/ShehanSulakshana)

---

> *"You can't defend what you can't see."*