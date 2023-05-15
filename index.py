from capitalpayments import SDK

sdk = SDK('your_api_key','your_api_secret')

# response = sdk.getCustomers()
# response = sdk.getItems()
# response = sdk.getItem({
#     'item_id' : 7
# })
# response = sdk.getCustomer({
#     'customer_id' : 2
# })

# response = sdk.createCustomer({
#     'name' : 'Javier',
#     'email' : 'javier.fernandez.pa93@gmail.cos',
#     'whatsapp' : '5213317361191',
#     'wallet' : 'TGeqgehNQhKwBferxpSKs9b4RgubtBDEnx',
# })
# response = sdk.createItem({
#     'title' : 'Mi item',
#     'description' : 'Mi descripción',
#     'price' : 123
# })
# response = sdk.createInvoices([
#     {
#         'invoice_id' : 'mi-1-1',
#         'amount' : 123
#     },
#     {
#         'invoice_id' : 'mi-1-2',
#         'amount' : 123
#     }
# ])
# response = sdk.createPayouts([
#     {
#         'payout_id' : 'mi-1-1',
#         'address' : 'TGeqgehNQhKwBferxpSKs9b4RgubtBDEnx',
#         'amount' : 123
#     },
#     {
#         'payout_id' : 'mi-1-2',
#         'address' : 'TGeqgehNQhKwBferxpSKs9b4RgubtBDEnx',
#         'amount' : 123
#     }
# ])

# print(response)