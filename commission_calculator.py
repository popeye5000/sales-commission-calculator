"""
Sales Commission Calculator
Calculates commission earned by each member of a sales team
Formula: Commission = Gross Sales * Commission Rate
"""

def calculate_commission(gross_sales, commission_rate):
    """
    Calculate commission for a single sales person
    
    Args:
        gross_sales (float): Total gross sales amount
        commission_rate (float): Commission rate as a decimal (e.g., 0.1 for 10%)
    
    Returns:
        float: Commission earned
    """
    return gross_sales * commission_rate


def get_sales_person_data():
    """
    Prompt user to input sales person data
    
    Returns:
        dict: Dictionary with name, gross_sales, and commission_rate
    """
    name = input("Enter sales person's name: ").strip()
    
    while True:
        try:
            gross_sales = float(input(f"Enter gross sales for {name}: $"))
            if gross_sales < 0:
                print("❌ Gross sales cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    while True:
        try:
            commission_rate = float(input(f"Enter commission rate for {name} (as decimal, e.g., 0.1 for 10%): "))
            if commission_rate < 0 or commission_rate > 1:
                print("❌ Commission rate should be between 0 and 1 (0% to 100%). Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    return {
        'name': name,
        'gross_sales': gross_sales,
        'commission_rate': commission_rate
    }


def display_commission_report(team_members):
    """
    Display a formatted report of commissions for all team members
    
    Args:
        team_members (list): List of dictionaries containing sales person data and commission
    """
    print("\n" + "="*75)
    print("SALES COMMISSION REPORT".center(75))
    print("="*75)
    print(f"{'Name':<20} {'Gross Sales':>15} {'Commission Rate':>15} {'Commission':>15}")
    print("-"*75)
    
    total_commission = 0
    for member in team_members:
        print(f"{member['name']:<20} ${member['gross_sales']:>14,.2f} {member['commission_rate']:>14.1%} ${member['commission']:>14,.2f}")
        total_commission += member['commission']
    
    print("-"*75)
    print(f"{'TOTAL COMMISSION':<20} {'':<15} {'':<15} ${total_commission:>14,.2f}")
    print("="*75 + "\n")


def main():
    """
    Main function to run the sales commission calculator
    """
    print("\n" + "🎯 Welcome to the Sales Commission Calculator! 🎯".center(50))
    print("="*50 + "\n")
    
    team_members = []
    
    while True:
        # Get number of sales people if first iteration
        if not team_members:
            while True:
                try:
                    num_people = int(input("How many sales people would you like to enter? "))
                    if num_people <= 0:
                        print("❌ Please enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")
        
        # Get data for each sales person
        if len(team_members) < num_people:
            print(f"\n📝 Entering data for sales person {len(team_members) + 1} of {num_people}:")
            print("-" * 50)
            person_data = get_sales_person_data()
            person_data['commission'] = calculate_commission(
                person_data['gross_sales'],
                person_data['commission_rate']
            )
            team_members.append(person_data)
        else:
            break
    
    # Display the report
    display_commission_report(team_members)
    
    # Ask if user wants to enter more data
    while True:
        another = input("Would you like to enter data for another sales person? (yes/no): ").strip().lower()
        if another in ['yes', 'y']:
            num_people += 1
            print(f"\n📝 Entering data for sales person {len(team_members) + 1}:")
            print("-" * 50)
            person_data = get_sales_person_data()
            person_data['commission'] = calculate_commission(
                person_data['gross_sales'],
                person_data['commission_rate']
            )
            team_members.append(person_data)
            display_commission_report(team_members)
        elif another in ['no', 'n']:
            print("\n✅ Thank you for using the Sales Commission Calculator!\n")
            break
        else:
            print("❌ Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
