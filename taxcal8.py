class taxcal:
    def __init__(self):
        self.income = 0

    def calculate(self):
        self.income = int(input("Enter the income:"))
        if self.income <= 50000:
            self.tax = 0
        elif self.income <= 60000 and self.income > 50000:
            self.tax = self.income * (10 / 100)
        elif self.income <= 150000 and self.income > 60000:
            self.tax = self.income * (20 / 100)
        elif self.income > 150000:
            self.tax = self.income * (30 / 100)
        return self.tax

def main():
    t1 = taxcal()
    t=t1.calculate()
    print(t)

if __name__ == '__main__':
    main()