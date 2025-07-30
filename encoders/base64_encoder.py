import base64

def encode(payload: str) -> str:
    return base64.b64encode(payload.encode()).decode()
