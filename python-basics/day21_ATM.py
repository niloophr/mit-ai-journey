INITIAL_BALANCE = 1000000        
MIN_WITHDRAWAL = 50000          
MAX_WITHDRAWAL_DAILY = 5000000  
MIN_BALANCE = 10000             
MAX_BALANCE = 100000000         

balance = INITIAL_BALANCE       
daily_withdrawn = 0             
choice = 0                      

print("=== Welcome to ATM System ===")
print(f"Your initial balance: {INITIAL_BALANCE:,} Tomans")

while True:  
    print("\n" + "="*30)
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    print("="*30)
    
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Error: Please enter a number between 1-4")
        continue  
    
    
    if choice == 1:
        print(f"\nCurrent Balance: {balance:,} Tomans")
        print(f"Today's Withdrawals: {daily_withdrawn:,} Tomans")
        print(f"Daily Withdrawal Limit Remaining: {MAX_WITHDRAWAL_DAILY - daily_withdrawn:,} Tomans")
    
    elif choice == 2:
        try:
            amount = int(input("Enter amount to withdraw: "))
            
            error_messages = []  
            
            if amount < MIN_WITHDRAWAL:
                error_messages.append(f"Minimum withdrawal is {MIN_WITHDRAWAL:,} Tomans")
            
            if balance - amount < MIN_BALANCE:
                error_messages.append(f"Minimum balance after withdrawal must be {MIN_BALANCE:,} Tomans")
            
            if daily_withdrawn + amount > MAX_WITHDRAWAL_DAILY:
                error_messages.append(f"Daily withdrawal limit exceeded! Maximum: {MAX_WITHDRAWAL_DAILY:,} Tomans")
            
            if amount <= 0:
                error_messages.append("Amount must be positive")
            
            if error_messages:
                print("\nWithdrawal Failed:")
                for error in error_messages:
                    print(f"  - {error}")
            else:
                balance -= amount
                daily_withdrawn += amount
                print(f"\nSuccess! {amount:,} Tomans withdrawn.")
                print(f"New Balance: {balance:,} Tomans")
                print(f"Today's Total Withdrawn: {daily_withdrawn:,} Tomans")
                
        except ValueError:
            print("Error: Please enter a valid number")
    
    elif choice == 3:
        try:
            amount = int(input("Enter amount to deposit: "))
            
            if amount <= 0:
                print("Error: Deposit amount must be positive")
            elif balance + amount > MAX_BALANCE:
                print(f"Error: Maximum account balance is {MAX_BALANCE:,} Tomans")
                print(f"Current balance: {balance:,} Tomans")
                print(f"Maximum deposit allowed: {MAX_BALANCE - balance:,} Tomans")
            else:
                balance += amount
                print(f"\nSuccess! {amount:,} Tomans deposited.")
                print(f"New Balance: {balance:,} Tomans")
                
        except ValueError:
            print("Error: Please enter a valid number")
    
    elif choice == 4:
        print("\nThank you for using our ATM!")
        print(f"Final Balance: {balance:,} Tomans")
        break  
    
    else:
        print("Error: Please select a valid option (1-4)")
