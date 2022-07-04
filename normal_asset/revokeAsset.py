from algosdk.future.transaction import AssetTransferTxn
from algosdk.future.transaction import *

from accountsService import accounts, algod_client
from functionService import print_asset_holding

asset_id=98318206

# REVOKE ASSET
# The clawback address (Account 2) revokes 10 latinum from Account 3 and places it back with Account 1.
params = algod_client.suggested_params()
# comment these two lines if you want to use suggested params
# params.fee = 1000
# params.flat_fee = True
# Must be signed by the account that is the Asset's clawback address

txn = AssetTransferTxn(
    sender=accounts[3]['pk'],
    sp=params,
    receiver=accounts[1]["pk"],
    amt=12,
    index=asset_id,
    revocation_target=accounts[3]['pk']
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
# The balance of account 3 should now be 0.
# account_info = algod_client.account_info(accounts[3]['pk'])
print("Account 3")
print_asset_holding(algod_client, accounts[3]['pk'], asset_id)
# The balance of account 1 should increase by 10 to 1000.
print("Account 1")
print_asset_holding(algod_client, accounts[1]['pk'], asset_id)


