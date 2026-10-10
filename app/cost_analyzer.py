
USD_TO_INR = 85.0


def analyze_costs(services_usd, budget_inr):
    services_inr = {
        service: cost * USD_TO_INR
        for service, cost in services_usd.items()
    }

    total_cost_inr = sum(services_inr.values())

    print("CloudSpend Guardian - Cost Report")
    print("---------------------------------")

    for service, cost in services_inr.items():
        print(f"{service}: ₹{cost:,.2f}")

    print("---------------------------------")
    print(f"Total cloud cost: ₹{total_cost_inr:,.2f}")
    print(f"Monthly budget: ₹{budget_inr:,.2f}")

    if total_cost_inr > budget_inr:
        print("ALERT: Monthly budget exceeded!")
    else:
        remaining = budget_inr - total_cost_inr
        print(f"Budget remaining: ₹{remaining:,.2f}")


if __name__ == "__main__":
    sample_services_usd = {
        "EC2": 45.50,
        "S3": 12.25,
        "RDS": 30.00,
    }

    monthly_budget_inr = 7000.00

    analyze_costs(sample_services_usd, monthly_budget_inr)
