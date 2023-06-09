# CapitalPayments
This Api has been made Crypto Payments based on USDT.TRC20
All examples are available into examples/ folder.

# Install with pip
> pip install capitalpayments

1. Create an account [Create account](capitalpayments.me/apps/signup "Create account")
2. Create api key [here](https://www.capitalpayments.co/apps/api/ "here")
3. Follow next steps to connect your account

(NOTE: Sandbox mode needs test coins request [here](https://www.capitalpayments.co/apps/api/ "here"))

# Login 

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

response = sdk.login()

```

# Get environment 

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get the environment : response >= int $sandobox (0 or 1)
response = sdk.getEnvironment()

```

# Get account

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get the account data
response = sdk.getAccount()

```

# Get balance

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get the balance from the api
response = sdk.getBalance()

```

# Get main wallet

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get main wallet data (private key is included)
response = sdk.getMainWallet()

```

# Get wallets

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# retrieves all wallets attached to api 
response = sdk.getWallets()

```
# Create invoice

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# retrieves invoice data
response = sdk.createInvoice({
    'invoice_id' : 'invoice_id' # string 
    'amount' : 'amount' # float|int 
    'whatsApp' : 'whatsApp' # (optional) int whatsapp full number
    'name' : 'customer_name' #  (optional) string customer's name
})

```
# Create invoices

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# retrieves invoices data
response = sdk.createInvoices([
    {
        'invoice_id' : 'invoice_id' # string 
        'amount' : 'amount' # float|int 
        'whatsApp' : 'whatsApp' # (optional) int whatsapp full number
        'name' : 'customer_name' #  (optional) string customer's name
    },
    {
        'invoice_id' : 'invoice_id' # string 
        'amount' : 'amount' # float|int 
        'whatsApp' : 'whatsApp' # (optional) int whatsapp full number
        'name' : 'customer_name' #  (optional) string customer's name
    }
])

```
# Get invoice status

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get the invoice status
response = sdk.getInvoiceStatus({
    'invoice_id' : 'invoice_id' # string 
})

```

# Cancel invoice

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get the invoice status
response = sdk.cancelInvoice({
    'invoice_id' : 'invoice_id' # string 
})

```

# Create payout

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# retrieve the payout data
response = sdk.createPayout({
    'payout_id' : 'payout_id' # string 
    'amount' : 'amount' # float|int 
    'address' : 'USDT.TRC20WalletAddress' # string
})

```

# Create payouts

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# retrieves payouts data
response = sdk.createPayouts([
    {
        'payout_id' : 'payout_id' # string 
        'amount' : 'amount' # float|int 
        'address' : 'USDT.TRC20WalletAddress' # string
    },
    {
        'payout_id' : 'payout_id' # string 
        'amount' : 'amount' # float|int 
        'address' : 'USDT.TRC20WalletAddress' # string
    },
])

```

# Get payout status

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get the payout status
response = sdk.getPayoutStatus({
    'payout_id' : 'payout_id' # string 
})

```

# Cancel payout 

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# cancel payout  
response = sdk.cancelPayout({
    'payout_id' : 'PayoutId', # @string
})

```

# create item

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# cancel payout  
response = sdk.createItem({
    'title' : 'title', # @string
    'description' : 'description', # @string
    'price' : 10 # @int|float
})
```

# delete item

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# delete item
response = sdk.deleteItem({
    'item_id' : 'item_id', # @string
})
```

# get items

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get array items
response = sdk.getItems()
```

# get item

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get item
response = sdk.getItem({
    'item_id' : 'item_id', # @string
})
```

# create customer

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# create customer
response = sdk.createCustomer({
    'name' : 'title', # @string
    'email' : 'description', # @string
    'whatsapp' : 'full_whatsapp', # @string
    'address' : 'USDT.TRC20WalletAddress', # @string
})
```

# delete customer

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# delete customer
response = sdk.deleteCustomer({
    'customer_id' : 'customer_id', # @string
})
```

# get customers

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get array customers
response = sdk.getCustomers()
```

# get customer

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# get customer by id
response = sdk.getCustomer({
    'customer_id' : 'customer_id', # @string
})
```

# set test invoice as payed

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# requires invoice_id
response = sdk.setTestInvoiceAsPayed({
    'invoice_id' : 'invoice_id'
})

```

# set deposit wallet

```

from sdk import SDK

sdk = SDK('api_key','api_secret')

# requires tron wallet address 
response = sdk.setDepositWallet({
    'address' : 'TTCkwzmTZHjN4VSVRVz7s1h5btjWGfvnF9'
})

```
