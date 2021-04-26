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


class inputDataAPIs:
    '''############### Class Variables ###############'''

    input_data_object = inputData()
    '''################## class API ##################'''

    #def __init__(self):
        # print("inputDataAPIs Class Constructor")

    def parseDebugModeValues(self):
        errorStatus = False

        # URL: https://www.zillow.com/homedetails/805-29th-St-APT-212-Boulder-CO-80303/13227452_zpid/

        # Home Details
        self.input_data_object.streetAddr  = str("3009 Madison Ave APT 112M")
        self.input_data_object.city        = str("Boulder")
        self.input_data_object.state       = str("CO")
        self.input_data_object.beds        = 2.0
        self.input_data_object.baths       = 2.0
        self.input_data_object.sqft        = 1102.0
        self.input_data_object.yearBuilt   = 1969

        # Purchase Details
        self.input_data_object.price       = 300000
        self.input_data_object.closingCost = 6000
        self.input_data_object.rehabCost   = 0
        self.input_data_object.homeAppreciation = 8
        # print("\n\n\t\tparseDebugModeValues(): price: ${}".format(self.input_data_object.price))

        # Loan Details
        self.input_data_object.dpPercent   = 20
        self.input_data_object.dpValue     = float((self.input_data_object.price * self.input_data_object.dpPercent)/100)
        self.input_data_object.interest    = 3.0
        self.input_data_object.loanTerm    = 30
        self.input_data_object.loanTermMonths = self.input_data_object.loanTerm * 12
        self.input_data_object.pmiPerMonth = 0

        # Rental Income Details
        self.input_data_object.monthlyRent    = 1750
        self.input_data_object.otherEarnings  = 0
        self.input_data_object.annualGrowth   = 3
        self.input_data_object.annualRentEarnings  = float(self.input_data_object.monthlyRent * 12)
        # print("\n\t\tparseDebugModeValues(): monthlyRent: ${}".format(self.input_data_object.monthlyRent))
        # print("parseDebugModeValues(): annualGrowth: ${}".format(self.input_data_object.annualGrowth))
        # print("parseDebugModeValues(): annualRentEarnings: ${}".format(self.input_data_object.annualRentEarnings))

        # Expenses
        # HOA 
        self.input_data_object.hoa     = 400
        # Insurance
        self.input_data_object.monthlyInsurance = 150
        # Property Taxes
        self.input_data_object.propertyTaxValue   = 2232
        self.input_data_object.propertyTaxPercent = float((self.input_data_object.propertyTaxValue * 100)/self.input_data_object.price)
        # Repairs and Maintenance
        self.input_data_object.rnmPercent = 5
        self.input_data_object.rnmValue   = float((self.input_data_object.annualRentEarnings * self.input_data_object.rnmPercent)/100)
        # Vacancy Rate
        self.input_data_object.vacancyRate = 3
        # Capital Expenditures
        self.input_data_object.capEx       = 5
        # Management Fees
        self.input_data_object.pmPercent = 0
        self.input_data_object.pmValue   = float((self.input_data_object.annualRentEarnings * self.input_data_object.pmPercent)/100)
        # Electricity 
        self.input_data_object.electricity = 0
        # Gas
        self.input_data_object.gas         = 0
        # Water/Sewer
        self.input_data_object.waterSewer  = 0
        # Garbage
        self.input_data_object.garbage     = 0
        # Other Costs
        self.input_data_object.other       = 0
        # Annual Expenses Growth
        self.input_data_object.expensesGrowth = 2
        # Sales Expenses
        self.input_data_object.salesExpenses  = 7.5

        return errorStatus

    def getManualInput(self):

        errorStatus = False
        print("\nEnter Home Details")
        self.input_data_object.streetAddr  = str(input("Enter Street Address: "))
        self.input_data_object.city        = str(input("City: "))
        self.input_data_object.state       = str(input("State: "))
        self.input_data_object.beds        = float(input("Number of Bedrooms: "))
        self.input_data_object.baths       = float(input("Number of Bathrooms: "))
        self.input_data_object.sqft        = float(input("Total sq.ft. value: "))
        self.input_data_object.yearBuilt   = int(input("Year Built: "))


        print("\nPurchase Details")
        self.input_data_object.price       = float(input("Enter Listed Home Price: $"))
        self.input_data_object.closingCost = float(input("Enter Closing Costs: $"))
        self.input_data_object.rehabCost   = float(input("Enter Rehab Costs: $"))
        self.input_data_object.homeAppreciation = float(input("Home Appreciation (in %): "))


        print("\nLoan Details")
        o = float(input("Downpayment Value in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.input_data_object.dpPercent = float(input("Enter Downpayment in %: "))
            self.input_data_object.dpValue   = float((self.input_data_object.price * self.input_data_object.dpPercent)/100)
            print("Corresponding Downpayment: ${}".format(self.input_data_object.dpValue))
        else:
            self.input_data_object.dpValue   = float(input("Enter Downpayment Value: $"))
            self.input_data_object.dpPercent = float((self.input_data_object.dpValue*100)/self.input_data_object.price)
            print("Corresponding Downpayment: {}%".format(dpPercent))
        self.input_data_object.interest    = float(input("Interest Rate (in %): "))
        self.input_data_object.loanTerm    = float(input("Loan Term (in years): "))
        self.input_data_object.loanTermMonths = self.input_data_object.loanTerm * 12
        self.input_data_object.pmiPerMonth = float(input("Personal Mortgage Insurance Per Month (PMI): $"))

        
        print("\nRental Income Details")
        self.input_data_object.monthlyRent    = float(input("Monthly Rent Earnings: $"))
        self.input_data_object.otherEarnings  = float(input("Other Earnings (Laundry/Parking): $"))
        self.input_data_object.annualGrowth   = float(input("Annual Rent Increase (in %): "))
        self.input_data_object.annualRentEarnings  = float(self.input_data_object.monthlyRent * 12)


        print("\nExpenses")
        # HOA 
        self.input_data_object.hoa     = float(input("HOA costs: $"))
        # Insurance
        self.input_data_object.monthlyInsurance = float(input("Monthly Insurance Costs: $"))
        # Property Taxes
        o = float(input("Property Tax Value (usually 0.6%) in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.input_data_object.propertyTaxPercent = float(input("Property Tax in %: "))
            self.input_data_object.propertyTaxValue   = float((self.input_data_object.price * self.input_data_object.propertyTaxPercent)/100)
            print("Corresponding Property Taxes: ${}".format(self.input_data_object.propertyTaxValue))
        else:
            self.input_data_object.propertyTaxValue   = float(input("Enter Property Tax Value: $"))
            self.input_data_object.propertyTaxPercent = float((self.input_data_object.propertyTaxValue * 100)/self.input_data_object.price)
            print("Corresponding Property Taxes: {}%".format(self.input_data_object.propertyTaxPercent))
        # Repairs and Maintenance
        o = float(input("Repairs and Maintenance Value in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.input_data_object.rnmPercent = float(input("Repairs and Maintenance Value in %: "))
            self.input_data_object.rnmValue   = float((self.input_data_object.monthlyRent * self.input_data_object.rnmPercent)/100)
            print("Repairs and Maintenance: ${}".format(self.input_data_object.rnmValue))
        else:
            self.input_data_object.rnmValue   = float(input("Repairs and Maintenance Value (per year): $"))
            self.input_data_object.rnmPercent = float((self.input_data_object.rnmValue * 100)/self.input_data_object.monthlyRent)
            print("Repairs and Maintenance: {}%".format(self.input_data_object.rnmPercent))
        # Vacancy Rate
        self.input_data_object.vacancyRate = float(input("Vacancy Rate (in %): "))
        # Capital Expenditures
        self.input_data_object.capEx       = float(input("Capital Expenditures (in %): "))
        # Management Fees
        o = float(input("Property Management Cost in \n(1) Percent Value of Home Price (%) or \n(2) Flat Amount ($)?\n"))
        if(o == 1):
            self.input_data_object.pmPercent = float(input("Property Management Cost in %: "))
            self.input_data_object.pmValue   = float((self.input_data_object.monthlyRent * self.input_data_object.pmPercent)/100)
            print("Corresponding Property Management: ${}".format(self.input_data_object.pmValue))
        else:
            self.input_data_object.pmValue   = float(input("Property Management Cost: $"))
            self.input_data_object.pmPercent = float((self.input_data_object.pmValue * 100)/self.input_data_object.monthlyRent)
            print("Corresponding Property Management: {}%".format(self.input_data_object.pmPercent))
        # Electricity 
        self.input_data_object.electricity = float(input("Average Electricity Costs (monthly): $"))
        # Gas
        self.input_data_object.gas         = float(input("Average Gas Costs (monthly): $"))
        # Water/Sewer
        self.input_data_object.waterSewer  = float(input("Water/Sewer Costs (monthly): $"))
        # Garbage
        self.input_data_object.garbage     = float(input("Average Garbage Costs (monthly): $"))
        # Other Costs
        self.input_data_object.other       = float(input("Other Costs (incl. Mello-Roos) (monthly): $"))
        # Annual Expenses Growth
        self.input_data_object.expensesGrowth = float(input("Average Annual Expenses Growth in % (generally 2%): "))
        # Sales Expenses
        self.input_data_object.salesExpenses  = float(input("Sales Expenses (How much will it cost to sell?) Enter value as a % of the final sale price (generally 7.5%): "))

        return errorStatus

    def getInput(self):

        errorStatus = False
        # Enter debug mode for regular analysis
        o = float(input("\nOptions:\n-> Enter Zillow URL or\n-> Enter '1' for Manual Mode \n-> Enter '2' for Debug Mode\nInput: "))
        if (o == 1):
            errorStatus = self.getManualInput()
            return (errorStatus)
        elif (o == 2):
            errorStatus = self.parseDebugModeValues()
            return (errorStatus)
        #else
            #errorStatus = self.parseUsingZillowURL(o)

        return errorStatus


class sharedMemory_Input:
    '''############### Class Variables ###############'''
    # inputObj = inputData()
    inputAPIsObj = inputDataAPIs()
    inputObj = inputAPIsObj.input_data_object

    ''' ###### class API ###### '''
    # def __init__(self):
        # print("Empty constructor for sharedMemory_Input")

    def getInputObj(self):
        return(self.inputObj)

    def getInputAPIsObj(self):
        return(self.inputAPIsObj)

    def display(self):
        print(inputObj)