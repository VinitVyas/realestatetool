'''
 * @file        impl.py
 * @ingroup     cal
 * @brief       Files containing internal/private APIs 
 *
 * Contains definitions of APIs specific to the cal state
 *
'''

from fsm.states.input.impl import sharedMemory_Input

class calData():
    '''################## class API ##################'''
    # def __init__(self):
        # print("Empty Constructor for calData class")

    def initialize(self):
        ipObj = sharedMemory_Input()
        self.i = ipObj.getInputObj()

        # Base Variables
        self.monthlyPAndI           = 0.0
        self.addlMonthlyExpenses    = 0.0
        self.totalMonthlyExpenses   = 0.0
        self.futureProofingExpenses = 0.0
        self.addlFixedExpenses      = 0.0
        self.addlVarExpenses        = 0.0
        self.cashFlow               = 0.0
        self.cashFlowYearly         = 0.0
        self.totalMonthlyEarnings   = 0.0
        self.noiMonthlyNoCapEx      = 0.0
        self.totalNOINoCapEx        = 0.0
        self.noiMonthly             = 0.0
        self.totalNOI               = 0.0
        self.totalInitialInvestment = 0.0
        self.cocReturns             = 0.0
        self.purchaseCapRate        = 0.0
        self.proFormaCapRate        = 0.0
        self.grm                    = 0.0

        # Derived Variables
        self.principal       = float(self.i.price - self.i.dpValue) 
        # print("\t\t\t\t\t\t\t\tCLASS VARIABLE: price {}".format(self.i.price))
        # print("\t\t\t\t\t\t\t\tCLASS VARIABLE: dpValue {}".format(self.i.dpValue))
        # print("\t\t\t\t\t\t\t\tCLASS VARIABLE: principal {}".format(self.principal))
        # print("\t\t\t\t\t\t\t\tCLASS VARIABLE: monthlyRent {}".format(self.i.monthlyRent))
        self.interestInVal   = float(self.i.interest / 100)
        self.numOfMonthsInYr = 12
        self.propertyTaxPerMonth = float(self.i.propertyTaxValue / 12)
        self.rnmValueMonthly     = float(self.i.rnmValue / 12)
        self.vacancyValueMonthly = float( (self.i.vacancyRate / 100) * self.i.monthlyRent )
        self.capExValueMonthly   = float( (self.i.capEx / 100) * self.i.monthlyRent )
        self.pmValueMonthly      = float( self.i.pmValue / 12 )
    
    def calculateMonthlyPrincipalAndInterest(self):
        ''' 
            Formula: Monthly P&I = (A * B * C) / (C - 1)
            A = Principal Amount
            B = [rate of interest / months in a year]
            C = [1 + (B)] ^ [months in a year * num of years]
        '''

        # print("calculateMonthlyPrincipalAndInterest(): principal: $", self.principal)
        A = self.principal
        B = float(self.interestInVal/self.numOfMonthsInYr)
        C = float(pow((1 + (B)), (self.numOfMonthsInYr * self.i.loanTerm)))

        numerator       = A * B * C

        if( (C - 1) != 0 ):
            denominator = C - 1
        else:
            denominator = 1

        monthlyPI = float(numerator / denominator)

        # Debug
        # print("\t\t\t\t\t\t\t\tprincipal : {}".format(self.principal))
        # print("rental_fsm_input_process(): ipObj {}".format(self.ipObj))
        # print("rental_fsm_input_process(): ii {}".format(self.i))
        # print("calculateMonthlyPrincipalAndInterest(): monthlyPI: ${}".format(self.monthlyPI))
        # print("calculateMonthlyPrincipalAndInterest(): monthlyRent ${}".format(self.monthlyRent))
        return monthlyPI

    def calculate(self):
        errorStatus = False
        # Initialize the values
        self.initialize()

        # 1. Cash Flow
        #    a. Calculate Monthly Earnings
        self.totalMonthlyEarnings   = self.i.monthlyRent + self.i.otherEarnings

        #    b. Calculate Monthly Expenses
        self.monthlyPAndI           = self.calculateMonthlyPrincipalAndInterest()

        self.addlFixedExpenses      = float(self.propertyTaxPerMonth + self.i.monthlyInsurance + self.i.hoa + self.i.pmiPerMonth)
        self.addlVarExpenses        = float(self.i.electricity + self.i.gas + self.i.waterSewer + self.i.garbage + self.i.other)
        self.futureProofingExpenses = float(self.rnmValueMonthly + self.vacancyValueMonthly + self.capExValueMonthly + self.pmValueMonthly)
        self.addlMonthlyExpenses    = float(self.addlFixedExpenses + self.addlVarExpenses + self.futureProofingExpenses)

        self.totalMonthlyExpenses   = self.monthlyPAndI + self.addlMonthlyExpenses

        self.cashFlow               = self.totalMonthlyEarnings - self.totalMonthlyExpenses
        self.cashFlowYearly         = self.cashFlow * 12
        # print("addlMonthlyExpenses: ${}".format(self.addlMonthlyExpenses))
        # print("monthlyPAndI: ${}".format(self.monthlyPAndI))
        # print("totalMonthlyExpenses: ${}".format(self.totalMonthlyExpenses))

        # 2. NOI
        self.noiMonthlyNoCapEx  = self.totalMonthlyEarnings - self.addlMonthlyExpenses + self.capExValueMonthly
        self.totalNOINoCapEx    = self.noiMonthlyNoCapEx * 12
        self.noiMonthly         = self.totalMonthlyEarnings - self.addlMonthlyExpenses
        self.totalNOI           = self.noiMonthly * 12

        # 3. CoC Returns
        self.totalInitialInvestment = self.i.dpValue + self.i.closingCost + self.i.rehabCost
        self.cocReturns         = float((self.cashFlowYearly * 100) / self.totalInitialInvestment)

        # 4. Cap rates
        self.purchaseCapRate    = float((self.totalNOI * 100) / self.i.price)
        self.proFormaCapRate    = float(( (self.totalNOI - self.i.rehabCost ) * 100)  / self.i.price)

        # 5. Gross Rent Multiplier
        self.grm                = float(self.i.price / self.i.annualRentEarnings)

        return errorStatus


class sharedMemory_Cal:
    '''############### Class Variables ###############'''
    calObj = calData()

    ''' ###### class API ###### '''
    # def __init__(self):
        # print("Empty constructor for sharedMemory_Cal")

    def getCalObj(self):
        return(self.calObj)

    def display(self):
        print(calObj)
