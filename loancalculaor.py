
import tkinter as tk
from tkinter import messagebox

class LoanCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Loan Calculator")
        
        self.client_name = tk.StringVar()
        self.loan_amount = tk.DoubleVar()
        self.years = tk.IntVar()
        self.interest_rate = tk.DoubleVar()
        
        self.create_widgets()

    def create_widgets(self):
        # Labels
        client_label = tk.Label(self.root, text="Client Name:")
        client_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        
        loan_label = tk.Label(self.root, text="Loan Amount ($):")
        loan_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        
        years_label = tk.Label(self.root, text="Number of Years:")
        years_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
        
        interest_label = tk.Label(self.root, text="Interest Rate (%):")
        interest_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")
        
        # Entry widgets
        client_entry = tk.Entry(self.root, textvariable=self.client_name)
        client_entry.grid(row=0, column=1, padx=5, pady=5)
        
        loan_entry = tk.Entry(self.root, textvariable=self.loan_amount)
        loan_entry.grid(row=1, column=1, padx=5, pady=5)
        
        years_entry = tk.Entry(self.root, textvariable=self.years)
        years_entry.grid(row=2, column=1, padx=5, pady=5)
        
        interest_entry = tk.Entry(self.root, textvariable=self.interest_rate)
        interest_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_payment)
        calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def calculate_payment(self):
        loan_amount = self.loan_amount.get()
        years = self.years.get()
        interest_rate = self.interest_rate.get()  # Intentional mistake: Not converting interest rate to a decimal
        
        monthly_interest = interest_rate / 12
        total_payments = years * 12
        # Intentional mistake: Incorrect formula for monthly payment calculation
        monthly_payment = loan_amount * (monthly_interest * (1 + monthly_interest) ** total_payments) / ((1 + monthly_interest) ** total_payments - 1)
        
        # Intentional mistake: Incorrect calculation for total payment
        total_payment = monthly_payment * total_payments
        
        messagebox.showinfo("Loan Details", "Monthly Payment: ${:.2f}\nTotal Payment: ${:.2f}".format(monthly_payment, total_payment))
        
root = tk.Tk()

# Intentional mistake: Misspelled class name when instantiating
loan_calculator = LoanCalculator(root)

root.mainloop()
