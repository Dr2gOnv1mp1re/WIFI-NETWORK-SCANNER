# WIFI-NETWORK-SCANNER
 Project 8: Wi-Fi Network Scanner  Problem Statement:  RISE  RISE  Users often need to check available networks and their signal  strength for optimal connectivity.  Objective:  Create a scanner that lists nearby Wi-Fi networks with basic  information such as signal strength.

📡 Wi-Fi Network Scanner - Windows

📝 About the Project
This is a lightweight Wi-Fi scanning tool built using Python and Tkinter, designed for Windows systems. It scans nearby Wi-Fi networks using the built-in Windows netsh command and displays the results in a simple graphical interface.

✨ Key Features


🔍 Quickly scans and lists available Wi-Fi networks

📶 Shows signal strength of each network

🚫 Filters out duplicate network names (SSIDs) for clarity

🖥️ Clean and responsive Tkinter GUI

⚙️ No third-party dependencies, only built-in Python modules and Windows commands



⚙️ How It Works


Executes the Windows command:
netsh wlan show networks mode=bssid

Parses the output using regular expressions

Extracts and displays:

SSID → Wi-Fi network name

Signal → Strength as a percentage

Displays results in a table view for easy reading

📋 Requirements


🪟 Windows OS (Windows 7, 8, 10, 11)

🐍 Python 3.x

📦 Standard Python libraries: tkinter, subprocess, re

🚀 How to Run


Open your Command Prompt or terminal

Navigate to your project folder



Run the script:

bash
Copy
Edit
python wifi_scanner.py
Click the Scan Wi-Fi button

View the list of available networks and their signal strength

⚠️ Limitations


🛑 Windows-only support, since it depends on the netsh command

🔐 Does not support connecting to networks, scanning only

❌ Hidden SSIDs will not appear in the scan results

🎯 Purpose


This project was created as a simple learning tool to demonstrate:

Creating desktop apps with Tkinter

Running system commands from Python

Parsing and displaying command-line output in a GUI
