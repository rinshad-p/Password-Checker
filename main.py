# main.py
from check_password import check_password_strength
from check_pwned import check_pwned
from colorama import init, Fore, Style
import time

# Initialize colorama for cross-platform colored output
init()

def print_header():
    print(f"{Fore.CYAN}{Style.BRIGHT}\n<========== Password Checker ==========>\n{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Test your password’s strength and check if it’s been leaked!{Style.RESET_ALL}")
    print("-" * 60)

def main():
    print_header()
    
    repeat = True  # Default value is True
    while repeat:
        # Get password input
        print(f"\n{Fore.WHITE}Enter The Password :{Style.RESET_ALL}", end=" ")
        password = input().strip()
        
        if not password:
            print(f"{Fore.RED}Error: Please enter a password.{Style.RESET_ALL}")
            continue
        
        # Strength check
        print(f"\n{Fore.CYAN}Checking strength...{Style.RESET_ALL}")
        time.sleep(1)
        strength_result = check_password_strength(password)
        if "Strong" in strength_result:
            print(f"{Fore.GREEN}{strength_result}{Style.RESET_ALL}")
        elif "Moderate" in strength_result:
            print(f"{Fore.YELLOW}{strength_result}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{strength_result}{Style.RESET_ALL}")
        
        # Breach check option
        print(f"{Fore.WHITE}Check if it’s been leaked? (y/n):{Style.RESET_ALL}", end=" ")
        check_breach = input().lower().strip()
        
        if check_breach == 'y':
            print(f"{Fore.CYAN}Checking breach status...{Style.RESET_ALL}")
            time.sleep(1)  # Small delay for "processing" feel
            breach_result = check_pwned(password)
            if "Warning" in breach_result:
                print(f"{Fore.RED}{breach_result}{Style.RESET_ALL}")
            elif "Good news" in breach_result:
                print(f"{Fore.GREEN}{breach_result}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}{breach_result}{Style.RESET_ALL}")
        
        # Ask if user wants to check another password
        print(f"\n{Fore.WHITE}Would you like to check another password? (y/n):{Style.RESET_ALL}", end=" ")
        repeat_response = input().lower().strip()
        repeat = (repeat_response == 'y')  # Update repeat based on user input
        
        if not repeat:
            print(f"{Fore.GREEN}Thanks for using the checker! Goodbye!{Style.RESET_ALL}")
        
        print("-" * 65)

if __name__ == "__main__":
    main()