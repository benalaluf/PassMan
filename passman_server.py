from src.connections.server_conn import ServerConn

passman_server= ServerConn(('127.0.0.1', 6969), ('127.0.0.1', 27017))
passman_server.accept_connections()
