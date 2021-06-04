def native_json(keypair_array):
    return str(keypair_array).replace(" ", "")


def keypair_array(hex_priv, hex_publ):
    return [int(b) for b in bytearray.fromhex(hex_priv + hex_publ)]

