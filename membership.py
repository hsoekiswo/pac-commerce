from tabulate import tabulate

class Member:
    membership_tiers = ['Platinum', 'Gold', 'Silver']
    membership_info = [
        ['Platinum', 0.15, 'Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%', 8, 15],
        ['Gold', 0.1, 'Benefit Silver + Voucher Ojek Online', 6, 10],
        ['Silver', 0.08, 'Voucher Makanan', 5, 7]
    ]
    info_headers = ['Membership', 'Discount', 'Another Benefit', 'Monthly Expense (juta)', 'Monthly Income (juta)']

    def show_benefit(self):
        benefit = []
        for i in self.membership_info:
            benefit.append(i[0:3])
        
        headers = self.info_headers[0:3]
        
        return print(tabulate(benefit, headers))