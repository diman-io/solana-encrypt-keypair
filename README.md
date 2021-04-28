# solana-encrypt-keypair

Tool for encrypt solana address and private key to native Solana keystore file.

## Usage
```
python3 solana-encrypt-keypair.py ADDRESS PRIVATE-KEY > wallet.json
```
## Sample

```
# python3 solana-encrypt-keypair.py 7GGqtUmwMbGEkx3JaTW5cr3SikfbvB5fhUyyEsDJHFfu 34aa423c3b230db24ac907b9161a331d30099df467ea4d99115705a5fd0f79c1 > exodus.json

# solana address -k exodus.json 
7GGqtUmwMbGEkx3JaTW5cr3SikfbvB5fhUyyEsDJHFfu
```