import json

from src.protocol.PacketData.PacketData import PacketData


class SessionPacketData(PacketData):
    def __init__(self, bytes=None, session_id=None):
        super().__init__()
        if bytes:
            self.data = json.loads(bytes.decode())
            self.session_id = self.data.get("session_id")
        else:
            self.session_id = session_id
            self.data = {
                "session_id": self.session_id
            }

    def __bytes__(self):
        json_str = json.dumps(self.data)
        return json_str.encode()

    def get_data(self):
        return self.data

    def get_session_id(self):
        return self.session_id
