import paramiko                                            


import socket


from queue import Queue


def port_scan(target, port):
    port_labels = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS", 
    }

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))


        if result ==0:
            service = port_labels.get(port, "OPEN")  
            print(f"Port {port}: {service} OPEN")

            








        elif result == 111 or result == 10061:
            print(f"Port {port}: CLOSED")


        else:
            print(f"Port {port}: Filtered (No response or timeout)")
        sock.close()

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")


    except socket.error as e:
        print(f"Socket error occurred: {e}")
        exit()







target = input("Enter the target IP Address or Domain:")

start_port = int(input("Enter the Start Port:"))

end_port = int(input("Enter the End Port:"))


for port in range(start_port, end_port + 1):
    port_scan(target,port)


print("\nPort scan complete.")
