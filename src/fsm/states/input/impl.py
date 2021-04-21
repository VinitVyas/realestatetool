'''
 * @file        impl.py
 * @ingroup     input
 * @brief       Files containing internal/private APIs for the input state
 *
 * Contains definitions of APIs specific to the input state
 *
'''

class inputData:
    '''############### Class Variables ###############'''


    '''################## class API ##################'''
    def __init__(self): 
        # print("inputData Class Constructor")

        # Home Details 
        self.streetAddr  = str("Default")
        self.city        = str("Default")
        self.state       = str("Default")
        self.beds        = 0.0
        self.baths       = 0.0
        self.sqft        = 0.0
        self.yearBuilt   = 0

        # Purchase Details
        self.price       = 0.0
        self.closingCost = 0.0
        self.rehabCost   = 0.0
        self.homeAppreciation = 0.0
        
        # Loan Details
        self.dpPercent   = 0.0
        self.dpValue     = 0.0
        self.interest    = 0.0
        self.loanTerm    = 0.0
        self.loanTermMonths = 0.0
        self.pmiPerMonth = 0.0
        
        # Rental Income Details
        self.monthlyRent = 0.0
        self.annualGrowth= 0.0
        self.annualRentEarnings = 0.0
        self.otherEarnings = 0.0
        
        # Expenses
        self.hoa         = 0.0
        self.monthlyInsurance   = 0.0
        self.propertyTaxPercent = 0.0
        self.propertyTaxValue   = 0.0
        self.rnmPercent  = 0.0
        self.rnmValue    = 0.0
        self.vacancyRate = 0.0
        self.capEx       = 0.0
        self.pmPercent   = 0.0
        self.pmValue     = 0.0
        self.electricity = 0.0
        self.gas         = 0.0
        self.waterSewer  = 0.0
        self.garbage     = 0.0
        self.other       = 0.0
        self.expensesGrowth = 0.0
        self.salesExpenses  = 0.0
        
    def debugModeValues(self):
        errorStatus = False

        # URL: https://www.zillow.com/homedetails/805-29th-St-APT-212-Boulder-CO-80303/13227452_zpid/

        # Home Details
        self.streetAddr  = str("3009 Madison Ave APT 112M")
        self.city        = str("Boulder")
        self.state       = str("CO")
        self.beds        = 2.0
        self.baths       = 2.0
        self.sqft        = 1102.0
        self.yearBuilt   = 1969

        # Purchase Details
        self.price       = 300000
        self.closingCost = 6000
        self.rehabCost   = 0
        self.homeAppreciation = 8
        # print("\n\n\t\tdebugModeValues(): price: ${}".format(self.price))

        # Loan Details
        self.dpPercent   = 20
        self.dpValue     = float((self.price * self.dpPercent)/100)
        self.interest    = 3.0
        self.loanTerm    = 30
        self.loanTermMonths = self.loanTerm * 12
        self.pmiPerMonth = 0

        # Rental Income Details
        self.monthlyRent    = 1750
        self.otherEarnings  = 0
        self.annualGrowth   = 3
        self.annualRentEarnings  = float(self.monthlyRent * 12)
        # print("\n\t\tdebugModeValues(): monthlyRent: ${}".format(self.monthlyRent))
        # print("debugModeValues(): annualGrowth: ${}".format(self.annualGrowth))
        # print("debugModeValues(): annualRentEarnings: ${}".format(self.annualRentEarnings))

        # Expenses
        # HOA 
        self.hoa     = 400
        # Insurance
        self.monthlyInsurance = 150
        # Property Taxes
        self.propertyTaxValue   = 2232
        self.propertyTaxPercent = float((self.propertyTaxValue * 100)/self.price)
        # Repairs and Maintenance
        self.rnmPercent = 5
        self.rnmValue   = float((self.annualRentEarnings * self.rnmPercent)/100)
        # Vacancy Rate
        self.vacancyRate = 3
        # Capital Expenditures
        self.capEx       = 5
        # Management Fees
        self.pmPercent = 0
        self.pmValue   = float((self.annualRentEarnings * self.pmPercent)/100)
        # Electricity 
        self.electricity = 0
        # Gas
        self.gas         = 0
        # Water/Sewer
        self.waterSewer  = 0
        # Garbage
        self.garbage     = 0
        # Other Costs
        self.other       = 0
        # Annual Expenses Growth
        self.expensesGrowth = 2
        # Sales Expenses
        self.salesExpenses  = 7.5

        return errorStatus

    def getInputFromUser(self):
        errorStatus = False
        
        # Enter debug mode for regular analysis
        o = float(input("(1) Regular Mode or \n(2) Debug Mode\nOption: "))
        if(o == 2):
            errorStatus = self.debugModeValues()
            return (errorStatus)

        print("\nEnter Home Details")
        self.streetAddr  = str(input("Enter Street Address: "))
        self.city        = str(input("City: "))
        self.state       = str(input("State: "))
        self.beds        = float(input("Number of Bedrooms: "))
        self.baths       = float(input("Number of Bathrooms: "))
        self.sqft        = float(input("Total sq.ft. value: "))
        self.yearBuilt   = int(input("Year Built: "))


        print("\nPurchase Details")
        self.price       = float(input("Enter Listed Home Price: $"))
        self.closingCost = float(input("Enter Closing Costs: $"))
        self.rehabCost   = float(input("Enter Rehab Costs: $"))
        self.homeAppreciation = float(input("Home Appreciation (in %): "))


        print("\nLoan Details")
        o = float(input("Downpayment Value in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.dpPercent = float(input("Enter Downpayment in %: "))
            self.dpValue   = float((self.price * self.dpPercent)/100)
            print("Corresponding Downpayment: ${}".format(self.dpValue))
        else:
            self.dpValue   = float(input("Enter Downpayment Value: $"))
            self.dpPercent = float((self.dpValue*100)/self.price)
            print("Corresponding Downpayment: {}%".format(dpPercent))
        self.interest    = float(input("Interest Rate (in %): "))
        self.loanTerm    = float(input("Loan Term (in years): "))
        self.loanTermMonths = self.loanTerm * 12
        self.pmiPerMonth = float(input("Personal Mortgage Insurance Per Month (PMI): $"))

        
        print("\nRental Income Details")
        self.monthlyRent    = float(input("Monthly Rent Earnings: $"))
        self.otherEarnings  = float(input("Other Earnings (Laundry/Parking): $"))
        self.annualGrowth   = float(input("Annual Rent Increase (in %): "))
        self.annualRentEarnings  = float(self.monthlyRent * 12)


        print("\nExpenses")
        # HOA 
        self.hoa     = float(input("HOA costs: $"))
        # Insurance
        self.monthlyInsurance = float(input("Monthly Insurance Costs: $"))
        # Property Taxes
        o = float(input("Property Tax Value (usually 0.6%) in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.propertyTaxPercent = float(input("Property Tax in %: "))
            self.propertyTaxValue   = float((self.price * self.propertyTaxPercent)/100)
            print("Corresponding Property Taxes: ${}".format(self.propertyTaxValue))
        else:
            self.propertyTaxValue   = float(input("Enter Property Tax Value: $"))
            self.propertyTaxPercent = float((self.propertyTaxValue * 100)/self.price)
            print("Corresponding Property Taxes: {}%".format(self.propertyTaxPercent))
        # Repairs and Maintenance
        o = float(input("Repairs and Maintenance Value in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.rnmPercent = float(input("Repairs and Maintenance Value in %: "))
            self.rnmValue   = float((self.monthlyRent * self.rnmPercent)/100)
            print("Repairs and Maintenance: ${}".format(self.rnmValue))
        else:
            self.rnmValue   = float(input("Repairs and Maintenance Value (per year): $"))
            self.rnmPercent = float((self.rnmValue * 100)/self.monthlyRent)
            print("Repairs and Maintenance: {}%".format(self.rnmPercent))
        # Vacancy Rate
        self.vacancyRate = float(input("Vacancy Rate (in %): "))
        # Capital Expenditures
        self.capEx       = float(input("Capital Expenditures (in %): "))
        # Management Fees
        o = float(input("Property Management Cost in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.pmPercent = float(input("Property Management Cost in %: "))
            self.pmValue   = float((self.monthlyRent * self.pmPercent)/100)
            print("Corresponding Property Management: ${}".format(self.pmValue))
        else:
            self.pmValue   = float(input("Property Management Cost: $"))
            self.pmPercent = float((self.pmValue * 100)/self.monthlyRent)
            print("Corresponding Property Management: {}%".format(self.pmPercent))
        # Electricity 
        self.electricity = float(input("Average Electricity Costs (monthly): $"))
        # Gas
        self.gas         = float(input("Average Gas Costs (monthly): $"))
        # Water/Sewer
        self.waterSewer  = float(input("Water/Sewer Costs (monthly): $"))
        # Garbage
        self.garbage     = float(input("Average Garbage Costs (monthly): $"))
        # Other Costs
        self.other       = float(input("Other Costs (incl. Mello-Roos) (monthly): $"))
        # Annual Expenses Growth
        self.expensesGrowth = float(input("Average Annual Expenses Growth in % (generally 2%): "))
        # Sales Expenses
        self.salesExpenses  = float(input("Sales Expenses (How much will it cost to sell?) Enter value as a % of the final sale price (generally 7.5%): "))

        return errorStatus

class sharedMemory_Input:
    '''############### Class Variables ###############'''
    inputObj = inputData()

    ''' ###### class API ###### '''
    # def __init__(self):
        # print("Empty constructor for sharedMemory_Input")

    def getInputObj(self):
        return(self.inputObj)

    def display(self):
        print(inputObj)