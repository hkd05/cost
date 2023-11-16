# Program to calculate fiber installation costs
# Author HKD
# 9/11/22


# total cost of installation with feet and rate (plus discounts)
def installation_cost(cable_feet, rate):
    total_cost = cable_feet * rate
    return total_cost


def main():
    # welcome message with a new line break
    print("Welcome to Ultra Shiny Fiber Company! "
          "\nPlease enter your information below to receive a total for your fiber installation project.")

    # retrieve company name from user
    companyName = input('What is your Company Name?\n')

    # retrieve number of cable feet
    cable_feet = float(input('How many feet of fiber optic cable will be installed?\n'))

    # determine discount rate
    if cable_feet < float(100):
        rate = .87
    elif cable_feet < float(250):
        rate = .80
    elif cable_feet < float(500):
        rate = .70
    elif cable_feet > float(500):
        rate = .50

    # calculate costs
    final_cost = installation_cost(cable_feet, rate)

    # format cost output
    formattedCost = '{:,.2f}'.format(final_cost)

    # print receipt with company name, total cable (in feet), total cost, and calculated cost
    print('Thank you,', companyName, '\nYour totals are below:')
    print('Total feet of fiber optic cable to be installed:', cable_feet, 'feet')
    print('Calculated Cost:', cable_feet, 'feet * $', rate,)
    print('Total Cost: $', formattedCost,)
    print('If you have any questions, please contact manager.')


main()
