from src.connections.client_conn import ClientConn
from src.gui.main_gui import ClientGUI


class ClientPassmanApp:
    def __init__(self, *args, **kwargs):
        self.conn = ClientConn()
        self.gui = ClientGUI()

    def main(self, ip, port):
        self.init_conn(ip, port)
        self.gui.main()

    def init_conn(self, ip, port):
        self.conn.connect_to_server(ip, port)


if __name__ == '__main__':
    app = ClientPassmanApp()
    app.main("127.0.0.1", 8080)
