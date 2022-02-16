# DCF stands for Discounted Cash Flow, an analysis method to find the price range for a stock.

# Free Cash Flow 209.7
# Avg of FCF = 140.36
# Growth Rate of 18%, 10%
# Discount rate of 9%
# number of year 10
years = 10
initialCapital = eval(input("Average Free Cash Flow in Crs(0==default):"))
if initialCapital == 0:
    initialCapital = 140.36
print("Average Cash Flow", initialCapital)
temp = initialCapital
growthRate1 = 18 * 0.01
growthRate2 = 10 * 0.01
terminalGrowthRate1 = 3.5 * 0.01
discountRate1 = 9 * 0.01
currentDebt = 75.94
cashBalance = 294.50
totalShares = 17.08
FutureCashFlow = []
PresentCashFlow = []



i=0
while i < 5: # Future Value
    i += 1
    initialCapital = initialCapital * (1 + growthRate1)
    FutureCashFlow.append(initialCapital)
while i < 10:
    i += 1
    initialCapital = initialCapital * (1 + growthRate2)
    FutureCashFlow.append(initialCapital)

for j in range(len(FutureCashFlow)): # Present Value
    PV = FutureCashFlow[j] / (1 + discountRate1)**(j+1)
    PresentCashFlow.append(PV)

terminalValue = FutureCashFlow[9] * (1 + terminalGrowthRate1) / (discountRate1 - terminalGrowthRate1) # Terminal Value
presentValueOfTV = terminalValue / (1+discountRate1)**10
totalFreeCashFlow = presentValueOfTV + sum(PresentCashFlow) # Total cash excluding debt
netDebt = currentDebt - cashBalance
totalPVofFCF = totalFreeCashFlow - netDebt
expectedShare = totalPVofFCF / totalShares

def percentage(x):
    return str(int(x*100))+"%"




growthStr = percentage(growthRate1) +" and " + percentage(growthRate2)
print(" Growth rate {0}, terminal growth {1}, discount rate {2}, net Debt (debt-cashBalance) = {3}.\n".format(growthStr, percentage(terminalGrowthRate1), percentage(discountRate1), netDebt))
print("|{:5s}|{:13s}|{:12s}|".format("Index","Present Value","Future Value"))
for i in range(10):
    print("|%5s|%13.2f|%12.2f|" %(i+1, FutureCashFlow[i], PresentCashFlow[i]))

print("\n---->Lower Middle Upper", round(expectedShare*0.8), round(expectedShare), round(expectedShare*1.2) )







'''
import tkinter as tk
import tksheet

# abc = [[f"{ri+cj}" for cj in range(4)] for ri in range(1)]
top = tk.Tk()

sheet = tksheet.Sheet(top)

sheet.grid()

data = ['Index', 'Future Value', 'Present Value', '3']
for j in range(10): data.append(['0', '1', '2', '3'])
sheet.set_sheet_data(data)

# table enable choices listed below:

sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu",
                       "rc_select", "rc_insert_row", "rc_delete_row", "copy", "cut", "paste", "delete", "undo",
                       "edit_cell"))
sheet.set_cell_data(0, 0, value = 10, redraw = False)

top.mainloop()
'''


