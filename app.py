# A simple, self-contained Python application (app.py) for calculating
# Compound Interest without external file input or continuous user interaction.

import math

def calculate_compound_interest(principal, rate, time, compounds_per_year):
    """
    Calculates the final amount and the interest earned using the compound interest formula.
    """
    try:
        base = 1 + (rate / compounds_per_year)
        exponent = compounds_per_year * time
        final_amount = principal * (base ** exponent)
        interest_earned = final_amount - principal
        return final_amount, interest_earned
        
    except ZeroDivisionError:
        print("Error: Compounds per year cannot be zero.")
        return 0.0, 0.0
    except TypeError:
        print("Error: All inputs must be numerical values.")
        return 0.0, 0.0
    except Exception as e:
        print(f"An unexpected error occurred during calculation: {e}")
        return 0.0, 0.0


def main():
    """
    Updated version of the compound interest calculator
    to test automatic Jenkins builds.
    """
    print(">>> This is an UPDATED VERSION of the Compound Interest Calculator!")
    print("--- Compound Interest Calculator (Updated Build Test) ---")
    
    # Predefined values
    P = 1000.0
    R = 0.05
    T = 10.0
    N = 4
    
    print(f"\nInvestment Details (Updated):")
    print(f"  Principal (P): ${P:,.2f}")
    print(f"  Annual Rate (r): {R*100:.1f}%")
    print(f"  Time (t): {T} years")
    print(f"  Compounding Frequency (n): {N} (Quarterly)")
    
    # Perform the calculation
    final_amount, interest_earned = calculate_compound_interest(P, R, T, N)
    
    if final_amount > 0:
        print("\n--- Updated Results ---")
        print(f"Final Amount (A): ${final_amount:,.2f}")
        print(f"Total Interest Earned: ${interest_earned:,.2f}")
        print("-----------------------------------------------")


if __name__ == "__main__":
    main()
