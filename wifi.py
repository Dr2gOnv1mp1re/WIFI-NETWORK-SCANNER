import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import re

def scan_wifi():
    tree.delete(*tree.get_children())
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            encoding="utf-8"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Could not scan Wi-Fi networks:\n{e}")
        return

    # Parse output
    networks = []
    ssid = None
    for line in output.splitlines():
        ssid_match = re.match(r'\s*SSID\s+\d+\s+:\s(.+)', line)
        if ssid_match:
            ssid = ssid_match.group(1).strip()
        signal_match = re.match(r'\s*Signal\s+:\s(\d+)%', line)
        if signal_match and ssid:
            signal = signal_match.group(1).strip()
            networks.append((ssid, signal))
    # Remove duplicates (SSID might appear several times if multiple BSSIDs)
    seen = set()
    unique_networks = []
    for ssid, signal in networks:
        if ssid not in seen:
            unique_networks.append((ssid, signal))
            seen.add(ssid)
    # Display in treeview
    for ssid, signal in unique_networks:
        tree.insert("", "end", values=(ssid, signal))

root = tk.Tk()
root.title("Wi-Fi Network Scanner")
root.geometry("400x350")

tk.Button(root, text="Scan Wi-Fi", command=scan_wifi, font=("Arial", 12)).pack(pady=10)

frame = ttk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("SSID", "Signal (%)")
tree = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180 if col == "SSID" else 100, anchor="center")
tree.pack(fill="both", expand=True)

root.mainloop()
