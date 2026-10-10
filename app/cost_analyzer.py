def validate_costs(services):
    for service, cost in services.items():
        if not isinstance(cost, (int, float)):
            raise ValueError(f"Invalid cost for {service}: cost must be a number")

        if cost < 0:
            raise ValueError(f"Invalid cost for {service}: cost cannot be negative")


USD_TO_INR = 85.0


def analyze_costs(services_usd, budget_inr):
    validate_costs(services_usd)
    
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
