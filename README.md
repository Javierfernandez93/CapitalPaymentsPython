# CapitalPayments
This Api has been made Crypto Payments based on USDT.TRC20
All examples are available into examples/ folder.

# Install with composer 
> composer require capitalpayments/sdk:dev-main

1. Create an account [Create account](capitalpayments.me/apps/signup "Create account")
2. Create api key [here](https://www.capitalpayments.co/apps/api/ "here")
3. Follow next steps to connect your account

(NOTE: Sandbox mode needs test coins request [here](https://www.capitalpayments.co/apps/api/ "here"))

# Login 

```

from sdk import SDK

sdk = SDK('api_key','api_secret');

response = sdk.login();

```

# Get environment 

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get the environment : response >= int $sandobox (0 or 1)
response = sdk.getEnvironment();

```

# Get account

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get the account data
response = sdk.getAccount();

```

# Get balance

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get the balance from the api
response = sdk.getBalance();

```

# Get main wallet

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get main wallet data (private key is included)
response = sdk.getMainWallet();

```

# Get wallets

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# retrives all wallets attached to api 
response = sdk.getWallets();

```

# Get invoice status

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get the invoice status
response = sdk.getInvoiceStatus({
    'invoice_id' => 'invoice_id' # string 
})

```

# Cancel invoice

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get the invoice status
response = sdk.cancelInvoice({
    'invoice_id' => 'invoice_id' # string 
})

```

# Create payout

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get the invoice status
response = sdk.createPayout({
    'payout_id' => 'payout_id' # string 
    'amount' => 'amount' # float|int 
})

```

# Get payout status

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# get the payout status
response = sdk.getPayoutStatus({
    'payout_id' => 'payout_id' # string 
})

```

# Cancel payout 

```

from sdk  SDK

sdk = SDK('api_key','api_secret');

# cancel payout  
response = sdk.cancelPayout({
    'payout_id' => 'PayoutId', # @string
})

```