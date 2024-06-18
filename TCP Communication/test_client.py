import socket

""" Client-side TCP communication on Python.
"""

IP = "127.0.0.1"
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    """ Establishes TCP socket with server, receives a message, appends its own
        message, sends it, then closes its socket.
    """
    # Create Client-side Socket Connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print("[CONNECTED] Successfully connected to Freq Server.")
    
    # Recieve a test message
    data = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] {data}")
    
    # Append & Send Message 
    data += " From CLIENT"
    client.send(data.encode(FORMAT))
    
    client.close()
    print("[SERVER] Connection closed.")


    
if __name__  == "__main__":
    main()

