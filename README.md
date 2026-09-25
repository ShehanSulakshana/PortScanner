# 🔍 PortScanner

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Purpose](https://img.shields.io/badge/Purpose-Educational-orange?style=flat)

A lightweight Python-based port scanner that detects open ports and running services on any host or IP address in real time. Built as a hands-on cybersecurity tool for network reconnaissance and vulnerability assessment practice.

> ⚠️ **For educational and authorized use only.** Never scan systems or networks without explicit permission. Unauthorized port scanning may be illegal in your jurisdiction.

---

## ✨ Features

- 🌐 Accepts both **IP addresses and domain names** (auto-resolves hostname to IP)
- 🎯 **Custom port range** scanning — target exactly what you need
- ⚡ **Real-time output** — open ports and services displayed as they're discovered
- 💾 **Export results** — save open ports and services to a `.txt` file
- 🏷️ **Service detection** — identifies the service running on each open port (e.g. HTTP, SSH, FTP)

---

## 📁 Files

| File | Description |
|---|---|
| `portscanner.py` | Main scanner script |
| `req.txt` | Python dependencies |

---

## ⚙️ Installation

```bash
git clone https://github.com/ShehanSulakshana/PortScanner.git
cd PortScanner
pip install -r req.txt
```

---

## 🚀 Usage

```bash
python portscanner.py
```

You'll be prompted for:

| Input | Example | Notes |
|---|---|---|
| Host / IP | `192.168.1.1` or `example.com` | Domains are auto-resolved to IP |
| Port range | `1-1024` | Larger ranges take more time |

---

## 📤 Sample Output

```
Scanning 192.168.1.1 from port 1 to 1024...

[OPEN]  Port 22   →  SSH
[OPEN]  Port 80   →  HTTP
[OPEN]  Port 443  →  HTTPS

Scan complete. 3 open ports found.
Save results to file? (y/n):
```

---

## 🛡️ Cybersecurity Context

Port scanning is a fundamental technique used in:

- **Penetration Testing** — mapping attack surfaces before an engagement
- **Network Administration** — auditing which services are exposed
- **CTF Challenges** — reconnaissance phase of any challenge
- **Vulnerability Assessment** — identifying potentially dangerous open ports

This tool provides the same core functionality as industry tools like `nmap`, built from scratch in Python to understand what's happening under the hood.

---

## 📜 License

[MIT](LICENSE)

---

## 👨‍💻 Author

**Shehan Sulakshana**  
Cybersecurity undergraduate | Python & Security enthusiast  
[GitHub](https://github.com/ShehanSulakshana)

---

> *"You can't defend what you can't see."* 🛡️
