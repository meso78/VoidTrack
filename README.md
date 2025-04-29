🛡️ VoidTrack | Cybersecurity Dark Army Knife

Track. Scan. Secure.


---

  

VoidTrack is an all-in-one network security toolkit combining IP geolocation, port scanning, packet sniffing, and threat detection in a single, user-friendly CLI.


---

🚀 Features

🌍 IP/Geo Tracking — Reveal the geographic locations of hidden IP addresses

🕵️ Port Scanner — Quickly and efficiently scan for open ports

📡 Packet Sniffer — Capture and analyze network traffic in real-time

🔥 Threat Detection — Identify suspicious activity and receive instant alerts



---

⚡ Installation Guide

Follow the steps below to get VoidTrack up and running on your system.

Prerequisites


Python 3.8+

Git

pip


Linux (Debian/Ubuntu)

sudo apt update && sudo apt install python3 python3-pip git -y

macOS

# Install Python if missing
brew install python@3.11

# Install Git
brew install git


---

Clone the Repository


git clone https://github.com/meso78/VoidTrack.git
cd VoidTrack

(Replace meso78 with your GitHub username if forked)


---

Set Up Virtual Environment


# Create a virtual environment
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate


---

Install Dependencies


pip install -r requirements.txt    # Install required packages
pip install -e .                   # Install VoidTrack in editable mode


---

Running VoidTrack


Option A: Interactive Launcher

python3 -m voidtrack.launcher

Option B: CLI Commands

# IP Geolocation
voidtrack ip 8.8.8.8 --detailed

# Port Scanning
voidtrack scan example.com -p 80,443,22 --threads 100

# Packet Sniffing (requires sudo/root)
sudo voidtrack sniff -i eth0 -d 30


---

Deactivate Virtual Environment


deactivate


---

Troubleshooting


Missing Python Packages?

pip install --force-reinstall -r requirements.txt

Permission Errors?

sudo chmod +x venv/bin/activate

Missing System Libraries (e.g., libpcap)?

# Linux
sudo apt install libpcap-dev

# macOS
brew install libpcap



---

Updating VoidTrack


git pull origin main
pip install --upgrade -r requirements.txt


---

Uninstall


cd .. && rm -rf VoidTrack


---

🔥 Usage Examples

# Track an IP addressoidtrack ip 8.8.8.8 --detailed
# Scan ports on a target host
voidtrack scan example.com -p 80,443,22
# Capture packets (requires sudo)
sudo voidtrack sniff -i wlan0 -d 60


---

🖼️ Demo

 Replace with real screenshot or GIF for best results.


---

🤝 Contributing

We welcome contributions! To set up a development environment:

git clone https://github.com/meso78/VoidTrack.git
cd VoidTrack
pip install -r requirements-dev.txt

See our Contribution Guide for details.


---

📜 License

This project is licensed under the Apache 2.0 License. See LICENSE for details.


---

💡 Pro Tip

# To exit the virtual environment
deactivate

Ready to become a cyber-ninja? 🥷 The network is your playground!
