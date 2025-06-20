import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import logging
from PIL import Image, ImageTk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import whois_lookup, dns_enum, subdomain_enum, port_scan, banner_grab, tech_detect
from utils import setup_logging

setup_logging(verbose=True)
logging.info("Informy GUI execution started...")

def run_recon():
    target = target_entry.get().strip()
    if not target:
        messagebox.showerror("Error", "Please enter a target domain or IP")
        return

    selected = {
        "WHOIS Information": whois_var.get(),
        "DNS Records": dns_var.get(),
        "Subdomains": subdomains_var.get(),
        "Open Ports": portscan_var.get(),
        "Banners": banner_var.get(),
        "Technologies": tech_var.get(),
    }

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"[+] Starting Recon on {target}...\n")
    run_button.config(state=tk.DISABLED)
    loading_label.config(text="Running reconnaissance...")
    progress_bar.start()

    def task():
        try:
            for name, enabled in selected.items():
                if enabled:
                    output_text.insert(tk.END, f"\n[ {name} ]\n")
                    if name == "WHOIS Information":
                        data = whois_lookup.run(target)
                    elif name == "DNS Records":
                        data = dns_enum.run(target)
                    elif name == "Subdomains":
                        data = subdomain_enum.run(target)
                    elif name == "Open Ports":
                        data = port_scan.run(target)
                    elif name == "Banners":
                        data = banner_grab.run(target)
                    elif name == "Technologies":
                        data = tech_detect.run(target)
                    else:
                        data = "Not implemented"
                    output_text.insert(tk.END, data + "\n")
        except Exception as e:
            output_text.insert(tk.END, f"\n[!] Error: {e}\n")
        finally:
            run_button.config(state=tk.NORMAL)
            loading_label.config(text="Recon complete.")
            progress_bar.stop()

    threading.Thread(target=task).start()

# GUI setup
root = tk.Tk()
root.title("Informy - Recon GUI")
root.geometry("800x750")
root.configure(bg="#f0f2f5")

# Logo
logo_path = os.path.join(os.path.dirname(__file__), '..', 'Informy-logo.png')
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((180, 60))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_photo, bg="#f0f2f5")
    logo_label.pack(pady=10)

# Author label
author_label = tk.Label(root, text="Developed by Hussain Amin Manj", font=("Helvetica", 10, "italic"), bg="#f0f2f5")
author_label.pack()

frame = tk.Frame(root, bg="#f0f2f5")
frame.pack(pady=20)

# Target input
tk.Label(frame, text="Target Domain/IP:", bg="#f0f2f5").grid(row=0, column=0, padx=5, pady=5, sticky="w")
target_entry = tk.Entry(frame, width=50)
target_entry.grid(row=0, column=1, padx=5, pady=5)

# Checkboxes
whois_var = tk.BooleanVar()
dns_var = tk.BooleanVar()
subdomains_var = tk.BooleanVar()
portscan_var = tk.BooleanVar()
banner_var = tk.BooleanVar()
tech_var = tk.BooleanVar()

options = [
    ("WHOIS Lookup", whois_var),
    ("DNS Enumeration", dns_var),
    ("Subdomain Enumeration", subdomains_var),
    ("Port Scanning", portscan_var),
    ("Banner Grabbing", banner_var),
    ("Technology Detection", tech_var),
]

for i, (label, var) in enumerate(options, start=1):
    tk.Checkbutton(frame, text=label, variable=var, bg="#f0f2f5").grid(row=i, column=1, sticky="w")

# Run button
run_button = tk.Button(root, text="Run Recon", command=run_recon, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20)
run_button.pack(pady=10)

loading_label = tk.Label(root, text="", font=("Helvetica", 10), fg="gray", bg="#f0f2f5")
loading_label.pack()

# Progress Bar
progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, mode='indeterminate', length=200)
progress_bar.pack(pady=5)

# Output text box
output_text = scrolledtext.ScrolledText(root, width=95, height=25, wrap=tk.WORD)
output_text.pack(padx=10, pady=10)

root.mainloop()
























# import os
# import sys
# import tkinter as tk
# from tkinter import ttk, messagebox, scrolledtext
# import threading
# import logging
# from PIL import Image, ImageTk

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from modules import whois_lookup, dns_enum, subdomain_enum, port_scan, banner_grab, tech_detect
# from utils import setup_logging

# setup_logging(verbose=True)
# logging.info("Informy GUI execution started...")

# def run_recon():
#     target = target_entry.get().strip()
#     if not target:
#         messagebox.showerror("Error", "Please enter a target domain or IP")
#         return

#     selected = {
#         "WHOIS Information": whois_var.get(),
#         "DNS Records": dns_var.get(),
#         "Subdomains": subdomains_var.get(),
#         "Open Ports": portscan_var.get(),
#         "Banners": banner_var.get(),
#         "Technologies": tech_var.get(),
#     }

#     output_text.delete(1.0, tk.END)
#     output_text.insert(tk.END, f"[+] Starting Recon on {target}...\n")
#     run_button.config(state=tk.DISABLED)
#     loading_label.config(text="Running reconnaissance...")

#     def task():
#         try:
#             for name, enabled in selected.items():
#                 if enabled:
#                     output_text.insert(tk.END, f"\n[ {name} ]\n")
#                     if name == "WHOIS Information":
#                         data = whois_lookup.run(target)
#                     elif name == "DNS Records":
#                         data = dns_enum.run(target)
#                     elif name == "Subdomains":
#                         data = subdomain_enum.run(target)
#                     elif name == "Open Ports":
#                         data = port_scan.run(target)
#                     elif name == "Banners":
#                         data = banner_grab.run(target)
#                     elif name == "Technologies":
#                         data = tech_detect.run(target)
#                     else:
#                         data = "Not implemented"
#                     output_text.insert(tk.END, data + "\n")
#         except Exception as e:
#             output_text.insert(tk.END, f"\n[!] Error: {e}\n")
#         finally:
#             run_button.config(state=tk.NORMAL)
#             loading_label.config(text="Recon complete.")

#     threading.Thread(target=task).start()

# # GUI setup
# root = tk.Tk()
# root.title("Informy - Recon GUI")
# root.geometry("800x700")
# root.configure(bg="#f0f2f5")

# # Logo
# logo_path = os.path.join(os.path.dirname(__file__), '..', 'Informy-logo.png')
# if os.path.exists(logo_path):
#     logo_img = Image.open(logo_path)
#     logo_img = logo_img.resize((180, 60))
#     logo_photo = ImageTk.PhotoImage(logo_img)
#     logo_label = tk.Label(root, image=logo_photo, bg="#f0f2f5")
#     logo_label.pack(pady=10)

# # Author label
# author_label = tk.Label(root, text="Developed by Hussain Amin Manj", font=("Helvetica", 10, "italic"), bg="#f0f2f5")
# author_label.pack()

# frame = tk.Frame(root, bg="#f0f2f5")
# frame.pack(pady=20)

# # Target input
# tk.Label(frame, text="Target Domain/IP:", bg="#f0f2f5").grid(row=0, column=0, padx=5, pady=5, sticky="w")
# target_entry = tk.Entry(frame, width=50)
# target_entry.grid(row=0, column=1, padx=5, pady=5)

# # Checkboxes
# whois_var = tk.BooleanVar()
# dns_var = tk.BooleanVar()
# subdomains_var = tk.BooleanVar()
# portscan_var = tk.BooleanVar()
# banner_var = tk.BooleanVar()
# tech_var = tk.BooleanVar()

# options = [
#     ("WHOIS Lookup", whois_var),
#     ("DNS Enumeration", dns_var),
#     ("Subdomain Enumeration", subdomains_var),
#     ("Port Scanning", portscan_var),
#     ("Banner Grabbing", banner_var),
#     ("Technology Detection", tech_var),
# ]

# for i, (label, var) in enumerate(options, start=1):
#     tk.Checkbutton(frame, text=label, variable=var, bg="#f0f2f5").grid(row=i, column=1, sticky="w")

# # Run button
# run_button = tk.Button(root, text="Run Recon", command=run_recon, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20)
# run_button.pack(pady=10)

# loading_label = tk.Label(root, text="", font=("Helvetica", 10), fg="gray", bg="#f0f2f5")
# loading_label.pack()

# # Output text box
# output_text = scrolledtext.ScrolledText(root, width=95, height=25, wrap=tk.WORD)
# output_text.pack(padx=10, pady=10)

# root.mainloop()
