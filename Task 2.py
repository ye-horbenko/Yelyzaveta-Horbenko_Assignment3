import json

deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08, # 8% річних
    "is_active": True
}

def new_balance(deposit_account) -> dict:
    suma = deposit_account["balance"] * deposit_account["interest_rate"]
    deposit_account["balance"] += suma
    deposit_account["last_update_type"] = "interest accrual"
    deposit_account["is_active"] = False
    return deposit_account

print(json.dumps(new_balance(deposit_account), indent=2))