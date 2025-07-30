def encode(payload: str) -> str:
    ascii_values = [str(ord(c)) for c in payload]
    return f"CHAR({','.join(ascii_values)})"
