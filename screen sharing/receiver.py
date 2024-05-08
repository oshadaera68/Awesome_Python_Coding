import threading

from vidstream import StreamingServer

receiver = StreamingServer('192.168.56.1', 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != "STOP":
    continue

receiver.stop_server()
