from coinbase.wallet.client import Client

client = Client("Ym8sRmWKERNmB2Ub","Ym8sRmWKERNmB2Ub",api_version='2016-05-23')

accounts = client.get_accounts()
for account in accounts.data:
  balance = account.balance
  print "%s: %s %s" % (account.name, balance.amount, balance.currency)
  print account.get_transactions()
