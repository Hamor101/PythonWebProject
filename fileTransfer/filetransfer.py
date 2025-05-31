import socket

class Transferer:
    addr = ""
    port = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, args):
        self.addr = args.address
        self.port = args.port
        self.filename = args.filename
    
    def send(self):
        self.sock.connect((self.addr, self.port))
        f = open(self.filename, "rb")
        content = f.read()
        self.sock.send(self.getFileName().encode())
        resp = self.sock.recv(4096).decode()
        if resp == "FNAME ACK":
            sent = self.sock.send(content)
            print(f"\033[44m[*]\033[0m {sent}/{len(content)} bytes sent.")
        else:
            print("\033[41m[*]\033[0m Could not transfer file contents.")
    
    def receive(self):
        self.sock.bind((self.addr, self.port))
        self.sock.listen(1)
        while True:
            
            cl, clAddr = self.sock.accept()
            data = b""
            fname = cl.recv(4096)
            if not fname:
                print("\033[41m[*]\033[0m Error receiving file name.")
                return
            cl.send("FNAME ACK".encode())
            f = open(fname, "wb")
            while True:
                buf = cl.recv(4096)
                data += buf
                if len(buf) < 4096:
                    print(f"\033[44m[*]\033[0m {len(data)} bytes received. Last transmission: {len(buf)} bytes.")
                    break
            cl.close()
            f.write(data)
            f.close()

    def getFileName(self):
        l = self.filename
        fname = ""
        for s in l[::-1]:
            if s == "/" or s == "\\":
                break
            else:
                fname += s
        return fname[::-1]
            
