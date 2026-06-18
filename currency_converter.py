EXCHANGE_RATES_TO_USD = {
    "USD": 1.0,
    "EUR": 1.08,    # 1 EUR = 1.08 USD
    "GBP": 1.27,    # 1 GBP = 1.27 USD
    "PLN": 0.25,    # 1 PLN = 0.25 USD
    "JPY": 0.0064,  # 1 JPY = 0.0064 USD
}

def convert_currency(amount, from_currency, to_currency):
    """Convert an amount from one currency to another using static rates.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
 
    from_code = from_currency.upper()
    to_code = to_currency.upper()
 
    if from_code not in EXCHANGE_RATES_TO_USD:
        raise ValueError(f"Unsupported currency: {from_currency}")
    if to_code not in EXCHANGE_RATES_TO_USD:
        raise ValueError(f"Unsupported currency: {to_currency}")
 
    # Convert amount -> USD -> target currency
    amount_in_usd = amount * EXCHANGE_RATES_TO_USD[from_code]
    converted = amount_in_usd / EXCHANGE_RATES_TO_USD[to_code]
    return round(converted, 2)
 
 
def list_supported_currencies():
    return sorted(EXCHANGE_RATES_TO_USD.keys())