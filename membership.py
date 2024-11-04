from tabulate import tabulate

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