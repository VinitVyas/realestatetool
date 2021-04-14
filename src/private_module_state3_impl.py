'''
 * @file        private_module_print.py
 * @ingroup     src
 * @brief       Files containing internal/private APIs for the current state
 *
 * Contains definitions of APIs specific to the current state
 *
'''

from private_module_state2_impl import sharedMemory_Cal
from private_module_state1_impl import sharedMemory_Input

class printData():
    '''################## class API ##################'''
    # def __init__(self):
        # print("Empty Constructor for printData class")

    def printAllData(self):
        errorStatus = False

        ipObj = sharedMemory_Input()
        i = ipObj.getInputObj()

        calObj = sharedMemory_Cal()
        c = calObj.getCalObj()

        print("|----------------------------------------------------------------|")
        print("|\t\t\t   Home Details   \t\t\t |")
        print("|----------------------------------------------------------------|")
        print("|\t Address: \t\t\t{}\t |".format(i.streetAddr))
        print("|\t City: \t\t\t\t{}\t\t\t |".format(i.city))
        print("|\t State: \t\t\t{}\t\t\t |".format(i.state))
        print("|\t Beds: \t\t\t\t{}\t\t\t |".format(i.beds))
        print("|\t Baths: \t\t\t{}\t\t\t |".format(i.baths))
        print("|\t Sq.ft: \t\t\t{}\t\t\t |".format(i.sqft))
        print("|\t Year Built: \t\t\t{}\t\t\t |".format(i.yearBuilt))
        print("|----------------------------------------------------------------|")
        print("\n\n")

        print("|------------------------------------------------------------------------|")
        print("|\t\t\t   Cash Flow   \t\t\t\t\t |")
        print("|------------------------------------------------------------------------|")
        print("Monthly Expenses")
        print("1. Principal & Interest: \t\t\t\t${:.2f}".format(c.monthlyPAndI))

        print("2. Additional Expenses")
        print("   a. Monthly Fixed Expenses: \t\t${:.2f}".format(c.addlFixedExpenses))
        print("     - Property Tax: \t\t${:.2f}".format(c.propertyTaxPerMonth))
        print("     - Insurance: \t\t${:.2f}".format(i.monthlyInsurance))
        print("     - HOA: \t\t\t${:.2f}".format(i.hoa))
        print("     - PMI: \t\t\t${:.2f}".format(i.pmiPerMonth))

        print("   b. Monthly Variable Expenses: \t${:.2f}".format(c.addlVarExpenses))
        print("     - Electricity: \t\t${:.2f}".format(i.electricity))
        print("     - Gas: \t\t\t${:.2f}".format(i.gas))
        print("     - Water/Sewer: \t\t${:.2f}".format(i.waterSewer))
        print("     - Garbage: \t\t${:.2f}".format(i.garbage))
        print("     - Other (monthly): \t${:.2f}".format(i.other))

        print("   c. Futureproofing Expenses: \t\t${:.2f}".format(c.futureProofingExpenses))
        print("     - Repairs & Maintenance: \t${:.2f}".format(c.rnmValueMonthly))
        print("     - Vacancy: \t\t${:.2f}".format(c.vacancyValueMonthly))
        print("     - Capital Expenditure: \t${:.2f}".format(c.capExValueMonthly))
        print("     - Property Management: \t${:.2f}".format(c.pmValueMonthly))
        print("   Total Additional Expenses\t\t\t\t${:.2f}".format(c.addlMonthlyExpenses))

        print("Total Monthly Expenses: \t\t\t\t\t${:.2f}".format(c.totalMonthlyExpenses))

        print("Monthly Earnings")
        print("  Rent Earnings (monthly): \t\t\t\t${:.2f}".format(i.monthlyRent))
        print("  Other Earnings (monthly): \t\t\t\t${:.2f}".format(i.otherEarnings))
        print("Total Monthly Earnings: \t\t\t\t\t${:.2f}".format(c.totalMonthlyEarnings))

        print("Total Cash Flow: \t\t\t\t\t\t${:.2f}".format(c.cashFlow))
        # print("\n\n")

        print("|------------------------------------------------------------------------|")
        print("|\t\t\t   Other Returns   \t\t\t\t |")
        print("|------------------------------------------------------------------------|")
        print("Monthly Net Operating Income (NOI) Without CapEx: \t${:.2f}".format(c.noiMonthlyNoCapEx))
        print("Net Operating Income (NOI) Without CapEx: \t\t\t${:.2f}".format(c.totalNOINoCapEx))
        print("Monthly Net Operating Income (NOI): \t\t\t${:.2f}".format(c.noiMonthly))
        print("Net Operating Income (NOI): \t\t\t\t\t${:.2f}\n".format(c.totalNOI))
        print("Cash-on-Cash Returns (CoC): \t\t\t\t\t{:.2f}%\n".format(c.cocReturns))
        print("Purchase Cap Rate: \t\t\t\t\t\t{:.2f}%".format(c.purchaseCapRate))
        print("Pro-forma Cap Rate: \t\t\t\t\t\t{:.2f}%\n".format(c.proFormaCapRate))
        print("Gross Rent Multiplier (GRM): \t\t\t\t\t{:.2f}".format(c.grm))

        print("|------------------------------------------------------------------------|")
        print("|\t\t\t         END      \t\t\t\t |")
        print("|------------------------------------------------------------------------|")

        return errorStatus


class SharedMemory_Print():
    '''############### Class Variables ###############'''
    printObj = printData()

    ''' ###### class API ###### '''
    # def __init__(self):
        # print("Empty constructor for sharedMemory_Print")

    def getPrintObj(self):
        return(self.printObj)

    def display(self):
        print(printObj)
