h = float(raw_input("Hours worked:"))
r = float(raw_input("Rate per hour:"))

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        overtime = hours - 40
        pay = 40 * rate + overtime * (rate * 1.5)
    return pay

print computepay(h, r)