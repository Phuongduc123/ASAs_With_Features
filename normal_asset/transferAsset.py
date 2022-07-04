from algosdk.future.transaction import AssetTransferTxn
from algosdk.future.transaction import *

from accountsService import accounts, algod_client
from functionService import print_asset_holding

asset_id=98318206

# TRANSFER ASSET
# transfer asset of 10 from account 1 to account 3
params = algod_client.suggested_params()
# comment these two lines if you want to use suggested params
# params.fee = 1000
# params.flat_fee = True
txn = AssetTransferTxn(
    sender=accounts[1]['pk'],
    sp=params,
    receiver=accounts[3]["pk"],
    amt=10,
    index=asset_id)
stxn = txn.sign(accounts[1]['sk'])
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
# The balance should now be 10.
print_asset_holding(algod_client, accounts[3]['pk'], asset_id)