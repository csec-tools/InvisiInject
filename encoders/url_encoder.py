from urllib.parse import quote

def encode(payload: str) -> str:
    return quote(payload)
