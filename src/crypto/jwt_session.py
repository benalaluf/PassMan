import secrets

import datetime

import jwt

from src.protocol.Packet import Packet
from src.protocol.PacketType import PacketType


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
        return None
    except jwt.InvalidTokenError:
        return None


def generate_secret_key(length=32):
    secret_key = secrets.token_hex(length)
    return secret_key


if __name__ == '__main__':
    print(generate_secret_key())
    niga = (generate_jwt("test", "test"))
    packetData = SessionPacketData(session_id=niga)
    packet = Packet(PacketType.SESSION, bytes(packetData))
