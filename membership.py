from tabulate import tabulate
import math

class Member:
    users_data = {
        1: ['Sumbul', 'Platinum'],
        2: ['Ana', 'Gold'],
        3: ['Cahya', 'Platinum']
    }

    membership_tiers = ['Platinum', 'Gold', 'Silver']
    membership_info = [
        ['Platinum', 0.15, 'Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%', 8, 15],
        ['Gold', 0.1, 'Benefit Silver + Voucher Ojek Online', 6, 10],
        ['Silver', 0.08, 'Voucher Makanan', 5, 7]
    ]
    info_headers = ['Membership', 'Discount', 'Another Benefit', 'Monthly Expense (juta)', 'Monthly Income (juta)']

    def __init__(self, username):
        self.username = username
        self.tier = None

        for key, value in self.users_data.items():
            if value[0] == self.username:
                self.tier = value[1]
                break


    def show_benefit(self):
        benefit = []
        for i in self.membership_info:
            benefit.append(i[0:3])
        
        headers = self.info_headers[0:3]
        
        return print(tabulate(benefit, headers))
    
    def show_requirements(self):
        requirements = [[i[0], i[3], i[4]] for i in self.membership_info]
        
        headers = [self.info_headers[i] for i in [0,3,4]]

        return print(tabulate(requirements, headers))
    
    def predict_membership(self, monthly_expense, monthly_income):
        silver_row = [i for i in self.membership_info if i[0] == 'Silver']
        silver_expense = silver_row[0][3]
        silver_income = silver_row[0][4]
        silver_pred = math.sqrt((monthly_expense - silver_expense)**2 + (monthly_income - silver_income)**2)

        gold_row = [i for i in self.membership_info if i[0] == 'Gold']
        gold_expense = gold_row[0][3]
        gold_income = gold_row[0][4]
        gold_pred = math.sqrt((monthly_expense - gold_expense)**2 + (monthly_income - gold_income)**2)

        platinum_row = [i for i in self.membership_info if i[0] == 'Platinum']
        platinum_expense = platinum_row[0][3]
        platinum_income = platinum_row[0][4]
        platinum_pred = math.sqrt((monthly_expense - platinum_expense)**2 + (monthly_income - platinum_income)**2)

        if(min(silver_pred, gold_pred, platinum_pred) == silver_pred):
            tier_prediction = 'Silver'
        elif(min(silver_pred, gold_pred, platinum_pred) == gold_pred):
            tier_prediction = 'Gold'
        elif(min(silver_pred, gold_pred, platinum_pred) == platinum_pred):
            tier_prediction = 'Platinum'

        if(self.tier not in self.membership_tiers):
            self.tier = tier_prediction
            return print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah (Platinum: {platinum_pred}, Gold: {gold_pred}, Silver: {silver_pred}) \n Kesimpulan Tier: {tier_prediction}")
        else:
            return print("Akun anda sudah teregistrasi")