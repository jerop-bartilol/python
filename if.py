basicPay=float(input("Enter the Basic Pay\n"))
houseAllowance=float(input("Enter the house allowance\n"))
commuterAllowance=float(input("Enter the commuter allowance\n"))

#Compute gross pay
grossPay=basicPay+houseAllowance+commuterAllowance

#Calculate PAYE
if grossPay >=0 and grossPay<=30000:
    paye=0.15*grossPay
    
if grossPay>=30001 and grossPay<=50000:
    paye=0.2*grossPay

if grossPay>50000:
    paye+0.25*grossPay
    
#Get the net pay
netPay=grossPay-paye

#output
print(f"Basic Pay\t{basicPay}\n")
print(f"House Allowance\t{houseAllowance}\n")
print(f"Commuter Allowance\t{commuterAllowance}\n")
print(f"Gross Pay\t{grossPay}\n")
print(f"P.A.Y.E\t{paye}\n")
print(f"Net Pay\t{netPay}\n")