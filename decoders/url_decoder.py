from urllib.parse import unquote

def decode(payload: str) -> str:
    return unquote(payload)
