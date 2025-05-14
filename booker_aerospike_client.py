import aerospike

config = {'hosts': [('10.212.47.173', 3000)]}
client = aerospike.client(config).connect()

client.get(('ns_256', 'review', '4aa8b2e6-4039-4328-b0bb-3bdb46a7ebb8'))

client.info_all('namespaces') # print all namespaces

client.info_all('sets') # print all sets

for i in client.query('ns_256', 'review').results():
  print(i[0])

