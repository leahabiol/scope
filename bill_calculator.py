def calculate_tip(bill, tip_percentage):
    return bill * tip_percentage * 0.01

def bill_total(bill, tip):
    return bill + tip

def bill_split(bill_total, num_guests):
    return bill_total / num_guests

def main():
    print "Enter 1 to calculate tip. Enter 2 to split the bill."
    choice = int(raw_input())
    
    if choice == 1:
        bill = float(raw_input("How much was the bill?" ))
        tip_percentage = float(raw_input("How much is the tip percentege? "))
        tip = calculate_tip(bill, tip_percentage)
        bill_total = bill_total(bill, tip)
        print "The tip is %f." % (tip)
        print "The bill is %f." % (bill_total)
        split = raw_input("Would you like to split the bill? Enter Y/N. ")
        if (split.upper() == "Y"):
            num_guests = int(raw_input("How many guests will be splitting the bill? "))
            bill_per_guest =  bill_split(bill_total, num_guests)
            print "Each person pays: %f." % (individual_bill)
    elif choice ==2:
        bill = float(raw_input("How much was the bill? "))
        num_guests = int(raw_input("How many guests will be splitting the bill? "))
        bill_per_guest =  bill_split(bill_total, num_guests)
        print "Each person pays: %f." % (individual_bill)

if __name__ == '__main__':
    print __name__
    main()       
