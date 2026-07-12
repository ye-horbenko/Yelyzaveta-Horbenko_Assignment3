import json

deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08, # 8% річних
    "is_active": True
}

def new_balance(deposit_accounts) -> dict:
    suma = deposit_accounts["balance"] * deposit_accounts["interest_rate"]
    deposit_accounts["balance"] += suma
    deposit_accounts["last_update_type"] = "interest accrual"
    deposit_accounts["is_active"] = False
    return deposit_accounts

print(json.dumps(new_balance(deposit_account), indent=2))