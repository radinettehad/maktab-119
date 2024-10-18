# import os
#
# remote_server = "google.com"
#
# if os.name == 'nt':
#     os.system(f"ping -n 5 {remote_server}")
# else:
#     os.system(f"ping -c 5 {remote_server}")

import subprocess
def ping(server, cont=5):
    command = ['ping', '-c', str(cont), server]
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    print(result.stdout)
ping("yahoo.com")
