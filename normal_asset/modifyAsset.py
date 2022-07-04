import json
import base64
from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn, AssetFreezeTxn
from algosdk.future.transaction import *

from accountsService import accounts, algod_client
from functionService import print_created_asset, print_asset_holding

# CHANGE MANAGER
# The current manager(Account 2) issues an asset configuration transaction that assigns Account 1 as the new manager.
# Keep reserve, freeze, and clawback address same as before, i.e. account 2
params = algod_client.suggested_params()
# comment these two lines if you want to use suggested params
# params.fee = 1000
# params.flat_fee = True

asset_id=98318206

txn = AssetConfigTxn(
    sender=accounts[1]['pk'],
    sp=params,
    index=asset_id,
    unit_name="OKE",
    manager=accounts[1]['pk'],
    reserve=accounts[2]['pk'],
    freeze=accounts[3]['pk'],
    clawback=accounts[3]['pk'])
# sign by the current manager - Account 2
stxn = txn.sign(accounts[1]['sk'])
# txid = algod_client.send_transaction(stxn)
# print(txid)
# Wait for the transaction to be confirmed
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
# Check asset info to view change in management. manager should now be account 1
print_created_asset(algod_client, accounts[1]['pk'], asset_id)