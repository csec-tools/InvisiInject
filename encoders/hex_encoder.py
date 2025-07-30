def encode(payload: str) -> str:
    return ''.join(f'\\x{ord(c):02x}' for c in payload)
