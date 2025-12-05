# A simple, self-contained Python application (app.py) for calculating
# Compound Interest without external file input or continuous user interaction.

import math

def calculate_compound_interest(principal, rate, time, compounds_per_year):
    """
    Calculates the final amount and the interest earned using the compound interest formula.
    
    Formula: A = P(1 + r/n)^(nt)
    Where:
        A = Final Amount
        P = Principal amount (initial investment)
        r = Annual interest rate (as a decimal)
        n = Number of times that interest is compounded per year
        t = Number of years the money is invested for

    Args:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate (e.g., 0.05 for 5%).
        time (float): The number of years.
        compounds_per_year (int): The compounding frequency (e.g., 12 for monthly).

    Returns:
        tuple: (final_amount, interest_earned)
    """
    try:
        # Calculate the base (1 + r/n)
        base = 1 + (rate / compounds_per_year)
        
        # Calculate the exponent (nt)
        exponent = compounds_per_year * time
        
        # Calculate the final amount (A)
        final_amount = principal * (base ** exponent)
        
        # Calculate the interest earned
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
    Main execution function to demonstrate the compound interest calculation
    with predefined values.
    """
    print("--- Compound Interest Calculator ---")
    
    # --- Define the Investment Parameters ---
    P = 1000.0  # Principal ($1,000)
    R = 0.05    # Annual Rate (5% or 0.05)
    T = 10.0    # Time in years (10 years)
    N = 4       # Compounds per year (Quarterly compounding)
    # ----------------------------------------
    
    print(f"\nInvestment Details:")
    print(f"  Principal (P): ${P:,.2f}")
    print(f"  Annual Rate (r): {R*100:.1f}%")
    print(f"  Time (t): {T} years")
    print(f"  Compounding Frequency (n): {N} (Quarterly)")
    
    # Perform the calculation
    final_amount, interest_earned = calculate_compound_interest(P, R, T, N)
    
    if final_amount > 0:
        print("\n--- Results ---")
        print(f"Final Amount (A): ${final_amount:,.2f}")
        print(f"Total Interest Earned: ${interest_earned:,.2f}")
        print("---------------")

# Standard Python entry point
if __name__ == "__main__":
    main()
