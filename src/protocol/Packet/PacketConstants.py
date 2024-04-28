class PacketConstants:
    # packet format
    # 0x/1 byte = type/4 byte = payload length/ payload

    TYPE_HEADER_FORMAT = '>B'  # big-big-endian unsigned char (1 byte)
    PAYLOAD_LENGTH_HEADER_FORMAT = '>I'  # big-endian unsigned int (4 byte)
    HEADER_LENGTH = 5  # bytes
    NO_DATA = b"none"
