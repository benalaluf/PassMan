from src.connections.server_conn import ServerConn

if __name__ == '__main__':
    server = ServerConn(('127.0.0.1', 3332), ('127.0.0.1', 27017))
    server.accept_connections()