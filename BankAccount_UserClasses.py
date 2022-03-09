class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):  #- increases the account balance by the given amount
        self.balance += amount
        return self
        
    def withdraw(self, amount): #-- decreases the account balance by the given amount if there are sufficient funds; 
        if self.balance - amount < 0: # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
            print ("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print ("Your account balance is $" + str("{:.2f}".format(self.balance))) #I found a way to ensure that the float always returns 2 decimal points
        return self

    def yield_interest(self):
        self.balance = (self.int_rate * self.balance) + self.balance
        return self
        

#This is the User Class that will be associated with these accounts
class User:		
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount) # the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount): #1 make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print (f"Hello, {self.name}") 
        self.account.display_account_info()
        return self                                                                 #and account balance to the terminal
                                                                                    #eg. "User: Guido van Rossum, Balance: $150


#Create 3 instances of the User class
danny = User("Danny", "dan@gmail.com")
sammy = User("Sammy", "sam@gmail.com")
mike = User("Michael", "mike@gmail.com")
#Have the first user make 3 deposits and 1 withdrawal and then display their balance
danny.make_deposit(25).make_deposit(100).make_deposit(75).make_withdrawal(125).display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
sammy.make_deposit(40).make_deposit(60).make_withdrawal(25).make_withdrawal(30).display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
mike.make_deposit(1200).make_withdrawal(200).make_withdrawal(200).make_withdrawal(500).display_user_balance()














dan_account = BankAccount(0.01, 5000) 
#make 3 deposits and 1 withdrawal, then yield interest and display the account's info
#  all in one line of code (i.e. chaining)
dan_account.deposit(200).deposit(130).deposit(40).withdraw(700).yield_interest().display_account_info()

#make 2 deposits and 4 withdrawals, then yield interest and display the 
# account's info all in one line of code (i.e. chaining)
sam_account = BankAccount(0.01, 2000)
sam_account.deposit(1400).deposit(593).withdraw(230).withdraw(103).withdraw(341).withdraw(123).yield_interest().display_account_info()

