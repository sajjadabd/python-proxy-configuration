import tkinter as tk
from tkinter import messagebox
import winreg
import subprocess

def set_proxy(proxy_server, port):
    try:
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        access = winreg.KEY_WRITE

        with winreg.OpenKey(key, subkey, 0, access) as internet_settings_key:
            winreg.SetValueEx(internet_settings_key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(internet_settings_key, "ProxyServer", 0, winreg.REG_SZ, f"{proxy_server}:{port}")
        
        # Open a CMD window and run the xray command
        cmd_command = "xray.exe"  # Replace with the actual xray command
        subprocess.Popen(["cmd", "/c", cmd_command])
        
        
        messagebox.showinfo("Proxy Set", "Proxy settings have been enabled.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def unset_proxy():
    try:
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        access = winreg.KEY_WRITE

        with winreg.OpenKey(key, subkey, 0, access) as internet_settings_key:
            winreg.SetValueEx(internet_settings_key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
            winreg.DeleteValue(internet_settings_key, "ProxyServer")

        messagebox.showinfo("Proxy Unset", "Proxy settings have been disabled.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Proxy Configuration")


# Set the window width to 200 pixels
window_width = 200
window_height = 140
root.geometry(f"{window_width}x{window_height}")


# Make the window non-resizable
root.resizable(False, False)

# Create widgets
label = tk.Label(root, text="Proxy Server:")

server_value = tk.StringVar()
server_value.set("127.0.0.1")

port_value = tk.StringVar()
port_value.set("10809")

entry = tk.Entry(root , textvariable=server_value )

port_label = tk.Label(root, text="Port:")

port_entry = tk.Entry(root , textvariable=port_value)
set_button = tk.Button(root, text="Set Proxy", command=lambda: set_proxy(entry.get(), port_entry.get()))
unset_button = tk.Button(root, text="Unset Proxy", command=unset_proxy)

# Arrange widgets
label.pack()
entry.pack()
port_label.pack()
port_entry.pack()
set_button.pack()
unset_button.pack()

# Run the Tkinter event loop
root.mainloop()