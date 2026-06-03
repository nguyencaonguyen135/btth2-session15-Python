atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balances():
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,.0f} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,.0f} VND")

def deposit_money(amount):
    global user_account_balance, atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount
    return True

def check_withdrawal_rules(amount):
    fee = 1100
    total_deduction = amount + fee
    
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS", total_deduction
    
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH", total_deduction
        
    return "OK", total_deduction

def execute_withdrawal(total_deduction, amount_to_dispense):
    global user_account_balance, atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,.0f} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,.0f} VND.")

def main():
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")
        
        choice = input("Vui lòng chọn giao dịch (1-4): ").strip()
        
        match choice:
            case '1':
                display_balances()
                
            case '2':
                print("\n--- NẠP TIỀN ---")
                amount_str = input("Nhập số tiền muốn nạp: ").strip()
                
                if not amount_str.isdigit():
                    print("Số tiền không hợp lệ.")
                    continue
                    
                amount = int(amount_str)
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                    continue
                    
                if deposit_money(amount):
                    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,.0f} VND.")
                    
            case '3':
                print("\n--- RÚT TIỀN ---")
                amount_str = input("Nhập số tiền cần rút: ").strip()
                
                if not amount_str.isdigit():
                    print("Số tiền không hợp lệ.")
                    continue
                    
                amount = int(amount_str)
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                    continue
                    
                if amount % 50000 != 0:
                    print("Số tiền rút phải là bội số của 50,000.")
                    continue
                    
                status, total_deduction = check_withdrawal_rules(amount)
                
                match status:
                    case "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Số dư tài khoản của bạn không đủ.")
                    case "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                    case "OK":
                        execute_withdrawal(total_deduction, amount)
                        
            case '4':
                print("\nCảm ơn quý khách đã sử dụng dịch vụ!")
                break
                
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 4.")

main()