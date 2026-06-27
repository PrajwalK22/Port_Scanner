from queue import Queue
import socket
import threading

q = Queue()
f = open("file.txt", "w", encoding="utf-8")

def port_scanner(port):
    s = socket.socket()
    s.settimeout(0.5)
    scan = s.connect_ex(("scanme.nmap.org", port))
    if scan == 0:
        print("The port is open: ", port)
        f.write("The port is open: " + str(port) + "\n")
        f.flush()
        if port == 80:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            Info = s.recv(1024).decode()
            print("HTTP detailed response: ", Info)
            f.write("HTTP detailed response: " + Info + "\n")
            f.flush()
        else:
            Info = s.recv(1024).decode()
            print("Additional Info: ", Info)
            f.write("Additional Info: " + Info + "\n")
            f.flush()
    s.close()

def worker_functionality():
    while True:
        try:
            port = q.get(block=False)
            port_scanner(port)
            q.task_done()
        except:
            break

for i in range(0, 1000):
    q.put(i)

for t in range(50):
    threading.Thread(target=worker_functionality).start()

q.join()
f.close()
