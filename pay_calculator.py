def computepay(h,r):
    additional_hours = h - 40;
    pay = h * r

    if additional_hours > 0:
        pay = pay - (additional_hours * r) + (additional_hours * (r * 1.5))

    return pay

try:
    hours = float(raw_input("Enter Hours:"))
    rate = float(raw_input("Enter Rate:"))
    print computepay(hours, rate)
except ValueError:
    print "Please enter numbers only"
