import sys
from datetime import datetime
import socket

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Please add a target host name or IP address: ")

print( "=" * 45)
print("Scan target: " + target)
print("Scanning started: " + str(datetime.now()))
print("=" * 45)

try:
    for port in range(1,1023):
        print(f"Scanning port {port}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        # Scan results
        result = s.connect_ex((target,port))

        if result ==0:
            print("Port number {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Scan halted by user.")
    sys.exit()