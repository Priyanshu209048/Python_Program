amount=float(input("Enter the amount: "))
if amount<=1000:
    discount=(amount)*(5/100)
    net_payable=amount-discount
    print("discount: ",discount)
    print("net payable: ",net_payable)
elif amount>=4000 and amount<=5000:
    discount=(amount)*(10/100)
    net_payable=amount-discount
    print("discount: ",discount)
    print("net payable: ",net_payable)
else:
    print("no discount")
    print("net payable: ",amount)
