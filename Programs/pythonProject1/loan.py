loan = 1000
interest_rate = 0.05

for year in range(1, 11):  # Years 1 to 10
    loan = loan + (loan * interest_rate)  # Or: loan *= 1.05
    print(f"Year {year}: Loan is now ${loan:.2f}")
