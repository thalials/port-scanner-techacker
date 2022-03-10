import socket
import time 

# fonte: https://docs.python.org/3/library/socket.html

def main(IP, initial_port, final_port):
    has_ports = False
    start = time.time()

    print(f"\nStarting connection to ({IP})\n")

    for PORT in range(initial_port, final_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                if s.connect_ex((IP, PORT)) == 0:
                    has_ports = True
                    SERVICE = socket.getservbyport(PORT)
                    # PROTOCOL = socket.getprotobyname("udp")
                    # if PROTOCOL == 6:
                    #     print("TCP")
                    # elif PROTOCOL == 17:
                    #     print("UDP")

                    print(f"PORT: {PORT} / RUNNING SERVICE: {SERVICE}")
            except OSError:
                continue

        s.close()

    if has_ports == False:
        print("\nThere are no services running in ports between this interval.")

    end = time.time()
    seconds = round(end-start, 2)

    print(f"\n1 IP address scanned in {seconds} seconds")

if __name__ == "__main__":
    IP = input("target's ID address: ")
    initial_port = int(input("Initial port: "))
    final_port = int(input("Final port: "))

    main(IP, initial_port, final_port)
		