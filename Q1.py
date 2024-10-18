import os

remote_server = "google.com"

if os.name == 'nt':
    os.system(f"ping -n 5 {remote_server}")
else:
    os.system(f"ping -c 5 {remote_server}")
