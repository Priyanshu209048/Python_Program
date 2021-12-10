vechile_cost=int(input("enter bike cost: "))
if vechile_cost<=50000:
    tax=(vechile_cost*5)/100
    print("road tax paid: ",tax)
elif vechile_cost>50000 and vechile_cost<=100000:
    tax=(vechile_cost*10)/100
    print("road tax paid: ",tax)
else:
    tax=(vechile_cost*15)/100
    print("road tax paid: ",tax)
