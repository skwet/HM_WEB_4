import threading
from socket_server import run_server
from web_server import  run

if __name__ == '__main__':
   
    sock = threading.Thread(target=run_server)
    web = threading.Thread(target=run)

    sock.start()
    web.start()

    sock.join()
    web.join()
   

    