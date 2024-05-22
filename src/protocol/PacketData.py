import json
from typing import Union, Optional


class PacketData:
    def __init__(self, data: Union[bytes, dict] = None):
        super().__init__()

        if isinstance(data, bytes):
            self.packet_data = json.loads(data.decode('utf-8'))
        else:
            self.packet_data = data

    def __bytes__(self):
        json_str = json.dumps(self.packet_data)
        return json_str.encode('utf-8')

    def get(self, key):
        try:
            return self.packet_data.get(key)
        except KeyError:
            print("packet key error")
            return None



if __name__ == '__main__':
    pass_data = PacketData({"url": "test", "username": "test", "password": "test", "date": "test"})
    print(pass_data.packet_data)
