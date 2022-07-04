from algosdk.v2client import algod
from algosdk import mnemonic

# Shown for demonstration purposes. NEVER reveal secret mnemonics in practice.
# Change these values with your mnemonics
mnemonic1 = "canyon lawsuit pull dry ethics limit silver scorpion rebuild permit dress series wet setup drill garbage battle indoor author require panic hawk hollow ability novel"
mnemonic2 = "bracket pizza try trade virus tone inflict poem display comic vivid envelope girl friend demise victory grape expand mansion ranch mind grain retreat able party"
mnemonic3 = "unfair scheme glimpse slight live rigid filter spend orange dish rich you number lonely fortune man vacuum point force quarter join birth embark above tenant"
# never use mnemonics in production code, replace for demo purposes only

# For ease of reference, add account public and private keys to
# an accounts dict.
accounts = {}
counter = 1
for m in [mnemonic1, mnemonic2, mnemonic3]:
    accounts[counter] = {}
    accounts[counter]['pk'] = mnemonic.to_public_key(m)
    accounts[counter]['sk'] = mnemonic.to_private_key(m)
    counter += 1

# Specify your node address and token. This must be updated.
algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = { 
    'X-API-Key': "djQJ9BZWlj8UCAjFOWDwvTBIrBE1UFX1qk7EtEn0"
}

algod_client = algod.AlgodClient(algod_token, algod_address, headers)