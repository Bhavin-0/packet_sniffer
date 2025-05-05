# 🚦 Network Traffic Monitoring & Classification Tool

## 📌 What This Project Does

This is a **basic cybersecurity tool** built using Python and Flask. It helps you:

✅ **Watch network traffic live** (who's sending or receiving data)
✅ **Understand the type of data** (TCP, UDP, ICMP, etc.)
✅ **Log and export traffic data** to a CSV file
✅ **Secure the dashboard** with a login system
✅ *(Coming soon)* Detect suspicious behavior like port scans

---

## 👥 Who Can Use This?

### 🔧 Network Admins

* Monitor network usage by devices
* Spot unusual or suspicious traffic

### 🛡️ Cybersecurity Learners/Analysts

* Learn protocol types and traffic patterns
* Use it for training or demonstrations

### 🧪 Students & Developers

* Debug network issues
* Learn about packet sniffing and web dashboards

---

## 🔍 Main Features Explained

| 💡 Feature                 | 📄 Description                             |
| -------------------------- | ------------------------------------------ |
| **Live Packet Monitoring** | Captures packets (data units) in real-time |
| **Traffic Classification** | Labels traffic by protocol (TCP/UDP/ICMP)  |
| **CSV Export**             | Save packet logs for later analysis        |
| **Web Dashboard**          | View live traffic in your browser          |
| **Login System**           | Secure the interface with authentication   |

---

## 🧰 Tech Stack

### 🐍 Python Libraries

* `scapy` → Captures network packets
* `flask` → Serves the dashboard as a web app
* `flask-login` → Handles user login and logout
* `csv` → Exports logs in CSV format

### 🖥️ Frontend

* **HTML/CSS + Bootstrap** → Styles and layout
* **Chart.js** → Displays traffic charts
* **JavaScript + jQuery** → Updates data dynamically

---

## 🔄 How It Works

1. **Start the app** using your terminal.
2. **Scapy captures packets** from your device.
3. **Data is processed and logged** (in memory and optionally saved).
4. **Flask serves a dashboard** you can access at `http://127.0.0.1:5000`
5. **You log in** to access traffic details and export options.

---

## 📂 How to Run the Project

### 1. Clone the repository

```bash
git clone <your_repo_url>
cd packetPatrol
```

### 2. Set up virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python3 main.py  # To start sniffing
python3 web_interface.py  # To launch dashboard
```

Then open your browser and go to:
👉 `http://127.0.0.1:5000`

Use the default credentials:

```
Username: admin
Password: admin123
```

---

## 🎯 Why It's Useful

* Gives insight into your network traffic
* Good starting point for learning network security
* Can be extended for deeper analysis and protection

---

## 🚀 Future Improvements

* 🌍 GeoIP Mapping (show country of IPs)
* 🤖 AI-Based threat detection
* 👥 Multi-user dashboard with access roles

---

**Created for learning and demonstration purposes.**
