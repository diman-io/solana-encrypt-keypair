import argparse
import base58
from common import native_json, keypair_array


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "ADDRESS",
        help='solana address from exodus wallet',
    )
    parser.add_argument(
        "PRIVATE_KEY",
        help="privake key from exodus wallet",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    b58_publ = args.ADDRESS
    hex_priv = args.PRIVATE_KEY
    
    hex_publ = base58.b58decode(b58_publ).hex()
    
    print(native_json(keypair_array(hex_priv, hex_publ)))


if __name__ == "__main__":
    main()
