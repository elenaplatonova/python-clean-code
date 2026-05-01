def process_payment(user, order):
    if user is not None:
        if user.get("is_active"):
            if order is not None:
                if order.get("total") > 0:
                    if order.get("total") <= user.get("credit_limit", 0):
                        charge = order["total"] * 1.08
                        return {"status": "ok", "charge": round(charge, 2)}
                    else:
                        return {"status": "error", "reason": "exceeds_credit"}
                else:
                    return {"status": "error", "reason": "invalid_total"}
            else:
                return {"status": "error", "reason": "no_order"}
        else:
            return {"status": "error", "reason": "inactive_user"}
    else:
        return {"status": "error", "reason": "no_user"}
