import argparse

from encoders import (
    url_encoder,
    base64_encoder,
    hex_encoder,
    char_encoder,
    space_encoder,
    comment_encoder
)

from decoders import (
    url_decoder,
    base64_decoder
)

ENCODERS = {
    "url": url_encoder.encode,
    "base64": base64_encoder.encode,
    "hex": hex_encoder.encode,
    "char": char_encoder.encode,
    "space": space_encoder.encode,
    "comment": comment_encoder.encode,
}

DECODERS = {
    "url": url_decoder.decode,
    "base64": base64_decoder.decode,
}


def apply_encoding_chain(payload: str, chain: list) -> str:
    for method in chain:
        encoder = ENCODERS.get(method.strip())
        if encoder:
            payload = encoder(payload)
        else:
            raise ValueError(f"Encoder '{method}' not found.")
    return payload


def apply_decoding_chain(payload: str, chain: list) -> str:
    for method in chain:
        decoder = DECODERS.get(method.strip())
        if decoder:
            payload = decoder(payload)
        else:
            raise ValueError(f"Decoder '{method}' not found.")
    return payload


def main():
    parser = argparse.ArgumentParser(description="InvisiInject - Encode/decode SQLi payloads")
    parser.add_argument("-p", "--payload", required=True, help="The SQL payload to encode/decode")
    parser.add_argument("--method", help="Encoding/decoding method to apply")
    parser.add_argument("--chain", help="Comma-separated list of encoding methods to chain")
    parser.add_argument("--decode", action="store_true", help="Switch to decoding mode")
    args = parser.parse_args()

    payload = args.payload
    methods = args.chain.split(",") if args.chain else ([args.method] if args.method else [])

    if not methods:
        print("❌ Error: You must specify at least one encoding or decoding method.")
        return

    try:
        if args.decode:
            result = apply_decoding_chain(payload, methods)
        else:
            result = apply_encoding_chain(payload, methods)

        print(result)
    except ValueError as ve:
        print(f"❌ {ve}")


if __name__ == "__main__":
    main()
