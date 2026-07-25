#Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
#ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

#print('Count:', data.count()) # 25
#print('Sum: ', data.sum()) # 744
#print('Min: ', data.min()) # 24
#print('Max: ', data.max()) # 38
#print('Range: ', data.range()) # 14
#print('Mean: ', data.mean()) # 30
#print('Median: ', data.median()) # 29
#print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
#print('Standard Deviation: ', data.std()) # 4.2
#print('Variance: ', data.var()) # 17.5
#print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
# you output should look like this
#print(data.describe())
#Count: 25
#Sum:  744
#Min:  24
#Max:  38
#Range:  14
#Mean:  30
#Median:  29
#Mode:  (26, 5)
#Variance:  17.5
#Standard Deviation:  4.2
#Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

#Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)

    def account_info(self):
        return f"First name: {self.firstname}\nLast name: {self.lastname}\nIncomes: {self.incomes}\nExpenses: {self.expenses}"

    def account_balance(self):
        return self.total_income() - self.total_expense()


account = PersonAccount('Asabeneh', 'Yetayeh')
account.add_income(1000, 'Salary')
account.add_income(500, 'Freelance work')
account.add_expense(200, 'Rent')
account.add_expense(100, 'Food')

print('Total Income:', account.total_income())
print('Total Expense:', account.total_expense())
print('Account Balance:', account.account_balance())
print(account.account_info())
