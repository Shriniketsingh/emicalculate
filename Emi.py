import streamlit as st

def calculate_emi(principal, rate_of_interest, tenure_years):
    # Convert annual rate to monthly and tenure to months
    monthly_rate = rate_of_interest / (12 * 100)
    tenure_months = tenure_years * 12

    # Calculate EMI
    emi = (principal * monthly_rate * ((1 + monthly_rate) ** tenure_months)) / (((1 + monthly_rate) ** tenure_months) - 1)
    return emi

def main():
    st.title("EMI Calculator")

    # Input fields
    principal = st.number_input("Loan Amount (Principal)", value=100000, step=1000)
    rate_of_interest = st.number_input("Annual Interest Rate (in %)", value=8.5, step=0.1)
    tenure_years = st.number_input("Loan Tenure (in years)", value=10, step=1)

    # Calculate button
    if st.button("Calculate EMI"):
        emi = calculate_emi(principal, rate_of_interest, tenure_years)
        st.success(f"Your monthly EMI is: ₹{emi:.2f}")

if __name__ == "__main__":
    main()
