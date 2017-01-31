#1st draft

BILL = 50
TIP_PERCENTAGE = 20
NUM_GUESTS = 2


def calculate_tip(TIP_PERCENTAGE):
    tip = TIP_PERCENTAGE * 0.01
    return tip

TIP = BILL * calculate_tip(TIP_PERCENTAGE)

def bill_total(BILL, TIP):
    bill_total = BILL + TIP
    return bill_total

TOTAL = bill_total(BILL, TIP)

def bill_split(TOTAL, NUM_GUESTS):
    individual_bill = TOTAL / NUM_GUESTS
    return individual_bill

print bill_split(TOTAL, NUM_GUESTS)




#2nd draft

def calculate_tip(bill, tip_percentage):
    tip = bill * tip_percentage * 0.01
    return tip

tip = calculate_tip(bill, tip_percentage)

def bill_total(bill, tip):
    bill_total = bill + (bill * tip)
    return bill_total

total = bill_total(bill, tip)

def bill_split(total, num_guests):
    individual_bill = total / num_guests
    return individual_bill

individual_bill = bill_split(total, num_guests)

def main():
    print "Enter 1 to calculate tip. Enter 2 to split the bill."