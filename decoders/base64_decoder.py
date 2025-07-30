import base64

def decode(payload: str) -> str:
    return base64.b64decode(payload.encode()).decode()
