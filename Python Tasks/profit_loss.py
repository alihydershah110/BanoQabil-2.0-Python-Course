# input selling price % cost price 
# then check seller has prpfit or loss or no prfit no loss
# determine loss & profit

cost_price=int(input("Enter cost price: "))
sell_price=int(input("Enter sell price: "))

if cost_price>sell_price:
    
    print("loss of: ",cost_price-sell_price)
elif cost_price<sell_price:
    print("Profit of: ",sell_price-cost_price)

else:
    print("No loss & NO profit..")
