from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn, AssetFreezeTxn
from algosdk.future.transaction import *

from accountsService import accounts, algod_client
from functionService import print_created_asset, print_asset_holding

asset_id=98318206

# FREEZE ASSET
params = algod_client.suggested_params()
# comment these two lines if you want to use suggested params
# params.fee = 1000
# params.flat_fee = True
# The freeze address (Account 2) freezes Account 3's latinum holdings.
txn = AssetFreezeTxn(
    sender=accounts[3]['pk'],
    sp=params,
    index=asset_id,
    target=accounts[2]["pk"],
    new_freeze_state=False
    )
stxn = txn.sign(accounts[3]['sk'])

# Send the transaction to the network and retrieve the txid.
try:
    txid = algod_client.send_transaction(stxn)
    print("Signed transaction with txID: {}".format(txid))
    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)  
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))    
except Exception as err:
    print(err)

# The balance should now be 10 with frozen set to true.
print_asset_holding(algod_client, accounts[2]['pk'], asset_id)