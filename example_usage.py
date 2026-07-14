from client import LoomalMcpBillingClient
client = LoomalMcpBillingClient()
print(client.charge_call("search_knowledge", 15, 0.02))