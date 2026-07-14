class LoomalMcpBillingClient:
    def charge_call(self, mcp_method: str, call_count: int, cost_per_call: float) -> dict:
        total = call_count * cost_per_call
        return {"charged_amount_usd": round(total, 4), "access_authorized": total < 10.0}