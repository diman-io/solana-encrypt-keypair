import argparse
import base58


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


def keypair_array(address, private_key):
    public_key = base58.b58decode(address.encode()).hex()
    return [int(b) for b in bytearray.fromhex(private_key + public_key)]


def main():
    args = parse_args()
    
    address = args.ADDRESS
    private_key = args.PRIVATE_KEY
    
    keypair = keypair_array(address, private_key)
    
    print(str(keypair).replace(" ", ""))


if __name__ == "__main__":
    main()
