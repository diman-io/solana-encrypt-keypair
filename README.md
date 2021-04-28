# solana-encrypt-keypair

Tool for encrypt Solana address and private key to native Solana keystore file.

## Usage
```
python3 solana-encrypt-keypair.py ADDRESS PRIVATE-KEY > wallet.json
```
## Sample

### Export private key from Exodus wallet
![image](https://user-images.githubusercontent.com/71597545/116482821-985d3600-a88e-11eb-9c06-b6ee9750c9ac.png)

### Encrypt data to native Solana keystore file
```
# python3 solana-encrypt-keypair.py 7GGqtUmwMbGEkx3JaTW5cr3SikfbvB5fhUyyEsDJHFfu 34aa423c3b230db24ac907b9161a331d30099df467ea4d99115705a5fd0f79c1 > exodus.json

# solana address -k exodus.json 
7GGqtUmwMbGEkx3JaTW5cr3SikfbvB5fhUyyEsDJHFfu
```
