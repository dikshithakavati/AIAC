def collect_customer_details():
    """Collect and return customer details"""
    print("Customer Details Collection")
    print("=" * 30)
    
    customer = {}
    
    customer['name'] = input("Enter customer name: ").strip()
    customer['customer_id'] = input("Enter customer ID: ").strip()
    customer['address'] = input("Enter address: ").strip()
    customer['phone'] = input("Enter phone number: ").strip()
    
    return customer

def show_previous_bill_details(customer):
    """Display previous bill details for the customer"""
    print(f"\nPrevious Bill Details for {customer['name']}")
    print("=" * 40)
    
    # Simulate previous bill data (in real scenario, this would come from database)
    previous_bills = [
        {"month": "January 2024", "units": 150, "amount": 450.00},
        {"month": "February 2024", "units": 180, "amount": 540.00},
        {"month": "March 2024", "units": 120, "amount": 360.00}
    ]
    
    if previous_bills:
        print(f"{'Month':<15} {'Units':<10} {'Amount (₹)':<12}")
        print("-" * 40)
        for bill in previous_bills:
            print(f"{bill['month']:<15} {bill['units']:<10} {bill['amount']:<12.2f}")
        
        # Calculate average
        total_units = sum(bill['units'] for bill in previous_bills)
        total_amount = sum(bill['amount'] for bill in previous_bills)
        avg_units = total_units / len(previous_bills)
        avg_amount = total_amount / len(previous_bills)
        
        print("-" * 40)
        print(f"{'Average':<15} {avg_units:<10.1f} {avg_amount:<12.2f}")
    else:
        print("No previous bill records found.")

def calculate_bill(units_consumed):
    """Calculate bill amount based on units consumed"""
    # Electricity tariff rates (₹ per unit)
    # First 100 units: ₹2.50 per unit
    # 101-200 units: ₹3.50 per unit  
    # 201-300 units: ₹4.50 per unit
    # Above 300 units: ₹5.50 per unit
    
    if units_consumed <= 100:
        rate = 2.50
        amount = units_consumed * rate
    elif units_consumed <= 200:
        amount = 100 * 2.50 + (units_consumed - 100) * 3.50
    elif units_consumed <= 300:
        amount = 100 * 2.50 + 100 * 3.50 + (units_consumed - 200) * 4.50
    else:
        amount = 100 * 2.50 + 100 * 3.50 + 100 * 4.50 + (units_consumed - 300) * 5.50
    
    # Add fixed charges and taxes
    fixed_charge = 50.00
    tax_rate = 0.05  # 5% tax
    tax_amount = amount * tax_rate
    
    total_amount = amount + fixed_charge + tax_amount
    
    return {
        'units': units_consumed,
        'energy_charge': amount,
        'fixed_charge': fixed_charge,
        'tax_amount': tax_amount,
        'total_amount': total_amount
    }

def display_current_bill(customer, bill_details):
    """Display the current bill in a formatted way"""
    print(f"\n" + "=" * 50)
    print(f"ELECTRICITY BILL")
    print("=" * 50)
    print(f"Customer Name: {customer['name']}")
    print(f"Customer ID: {customer['customer_id']}")
    print(f"Address: {customer['address']}")
    print(f"Phone: {customer['phone']}")
    print(f"Bill Date: {__import__('datetime').datetime.now().strftime('%d/%m/%Y')}")
    print("-" * 50)
    print(f"{'Description':<25} {'Amount (₹)':<15}")
    print("-" * 50)
    print(f"{'Energy Charges':<25} {bill_details['energy_charge']:<15.2f}")
    print(f"{'Fixed Charges':<25} {bill_details['fixed_charge']:<15.2f}")
    print(f"{'Tax (5%)':<25} {bill_details['tax_amount']:<15.2f}")
    print("-" * 50)
    print(f"{'TOTAL AMOUNT':<25} {bill_details['total_amount']:<15.2f}")
    print("=" * 50)

def main():
    """Main program function"""
    print("Power Bill Calculator")
    print("=" * 25)
    
    while True:
        print("\n1. Calculate New Bill")
        print("2. View Previous Bills")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Collect customer details
            customer = collect_customer_details()
            
            # Get current month's units consumed
            try:
                units = float(input(f"\nEnter units consumed for {customer['name']}: "))
                if units < 0:
                    print("Units consumed cannot be negative!")
                    continue
                    
                # Calculate bill
                bill_details = calculate_bill(units)
                
                # Display bill
                display_current_bill(customer, bill_details)
                
                # Show previous bills for comparison
                show_previous_bill_details(customer)
                
            except ValueError:
                print("Please enter a valid number for units consumed.")
                
        elif choice == '2':
            if 'customer' in locals():
                show_previous_bill_details(customer)
            else:
                print("Please calculate a bill first to view previous bills.")
                
        elif choice == '3':
            print("\nThank you for using Power Bill Calculator!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()