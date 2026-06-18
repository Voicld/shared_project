"""
Personal Finance Tool
======================
Core module (owned by Lead): savings growth and interest calculations.
Currency conversion (added by Junior) is wired in via currency_converter.py.
"""

from currency_converter import convert_currency


def simple_interest(principal, annual_rate_percent, years):
    """Calculate simple interest earned over a number of years.

    principal: starting amount
    annual_rate_percent: annual interest rate as a percentage (e.g. 5 for 5%)
    years: number of years
    """
    if principal < 0 or annual_rate_percent < 0 or years < 0:
        raise ValueError("principal, rate, and years must be non-negative")
    interest = principal * (annual_rate_percent / 100) * years
    return round(interest, 2)


def compound_interest(principal, annual_rate_percent, years, times_per_year=1):
    """Calculate the final balance after compound interest.

    times_per_year: how many times interest compounds per year (1 = annually,
                     12 = monthly, 365 = daily)
    """
    if principal < 0 or annual_rate_percent < 0 or years < 0 or times_per_year <= 0:
        raise ValueError("principal, rate, years must be non-negative and "
                          "times_per_year must be positive")
    rate = annual_rate_percent / 100
    final_amount = principal * (1 + rate / times_per_year) ** (times_per_year * years)
    return round(final_amount, 2)


def savings_goal_months(target_amount, monthly_contribution, current_savings=0):
    """Calculate how many months it will take to reach a savings goal,
    assuming a fixed monthly contribution and no interest.
    """
    if monthly_contribution <= 0:
        raise ValueError("monthly_contribution must be positive")
    if current_savings >= target_amount:
        return 0

    remaining = target_amount - current_savings
    months = remaining / monthly_contribution
    # Round up: you need a full month's contribution to cross the line
    import math
    return math.ceil(months)


def display_menu():
    print("=== Personal Finance Tool ===")
    print("1. Simple Interest Calculator")
    print("2. Compound Interest Calculator")
    print("3. Savings Goal Planner")
    print("4. Currency Converter")
    print("5. Net Worth Tracker (coming soon)")
    print("0. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            p = float(input("Principal amount: "))
            r = float(input("Annual interest rate (%): "))
            y = float(input("Number of years: "))
            print(f"Simple interest earned: {simple_interest(p, r, y)}")

        elif choice == "2":
            p = float(input("Principal amount: "))
            r = float(input("Annual interest rate (%): "))
            y = float(input("Number of years: "))
            n = int(input("Compounds per year (1=annual, 12=monthly): "))
            print(f"Final balance: {compound_interest(p, r, y, n)}")

        elif choice == "3":
            target = float(input("Target savings goal: "))
            monthly = float(input("Monthly contribution: "))
            current = float(input("Current savings (0 if none): "))
            months = savings_goal_months(target, monthly, current)
            print(f"Months needed to reach goal: {months}")

        elif choice == "4":
            amt = float(input("Amount: "))
            src = input("From currency (e.g. USD): ").strip()
            dst = input("To currency (e.g. EUR): ").strip()
            print(f"Converted amount: {convert_currency(amt, src, dst)}")

        elif choice == "5":
            print("Net Worth Tracker is coming in a future release!")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()