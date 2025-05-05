amount = 0

net_units = float(input('Enter your unit value : '))

if net_units <= 100:
    amount = 0  # Corrected the typo 'amonut' to 'amount'
    
elif net_units > 100 and net_units <= 200:
    amount = (net_units - 100) * 5
    
elif net_units > 200:
    amount = ((net_units - 200) * 10) + 500

print('Amount is ', amount)
