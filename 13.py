
class Account:
    def __init__(self, holder, money):
        self.holder = holder
        self.__money = money

    def add_money(self, amount):
        if amount > 0:
            self.__money += amount
            print("Deposit completed.")
        else:
            print("Invalid amount!")

    def remove_money(self, amount):
        if 0 < amount <= self.__money:
            self.__money -= amount
            print("Money withdrawn successfully.")
        else:
            print("Insufficient funds!")

    def balance(self):
        return self.__money

    def account_info(self):
        print("Holder Name:", self.holder)
        print("Available Balance:", self.balance())


class Savings(Account):
    def __init__(self, holder, money, rate):
        super().__init__(holder, money)
        self.rate = rate

    def account_info(self):
        super().account_info()
        print("Savings Interest:", self.rate, "%")


class Current(Account):
    def __init__(self, holder, money, overdraft):
        super().__init__(holder, money)
        self.overdraft = overdraft

    def account_info(self):
        super().account_info()
        print("Overdraft Facility:", self.overdraft)


user = input("Enter account holder name: ")
initial = float(input("Enter initial balance: "))

bank = Savings(user, initial, 5)

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Balance")
    print("4. Display Account")
    print("5. Exit")

    option = input("Choose option: ")

    if option == "1":
        bank.add_money(float(input("Enter amount: ")))

    elif option == "2":
        bank.remove_money(float(input("Enter amount: ")))

    elif option == "3":
        print("Your Balance:", bank.balance())

    elif option == "4":
        bank.account_info()

    elif option == "5":
        print("Thank you! Visit Again.")
        break

    else:
        print("Please enter a valid option.")
