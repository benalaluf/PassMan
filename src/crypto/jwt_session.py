import secrets

import jwt
import datetime

from src.protocol.Packet.Packet import Packet
from src.protocol.Packet.PacketType import PacketType
from src.protocol.PacketData.SessionPacketData import SessionPacketData


def generate_jwt(username, secret_key):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

    payload = {
        'username': username,
        'exp': expiration_time
    }

    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')

    return jwt_token


def verify_jwt(jwt_token, secret_key):
    try:
        payload = jwt.decode(jwt_token, secret_key, algorithms=['HS256'])
        return payload['username']
    except jwt.ExpiredSignatureError:
        return "Token is expired"
    except jwt.InvalidTokenError:
        return "Invalid token"


def generate_secret_key(length=32):
    secret_key = secrets.token_hex(length)
    return secret_key


if __name__ == '__main__':
    print(generate_secret_key())
    niga = (generate_jwt("test", "test"))
    packetData = SessionPacketData(session_id=niga)
    packet = Packet(PacketType.SESSION, bytes(packetData))
