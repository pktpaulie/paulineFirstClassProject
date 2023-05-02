'''
First Python Class Project
This program processes sales orders for an auto shop that
sells spare/ repair parts and computes appropriate output
information.

- use dynamic functions
- orders made by phone
- application computes output information

Customer
- customer ID, name, town code
- retail - 'ret' and wholesale customers - 'who'

Part ordered
- part number, description, price per part, quantity, oversize order status
shipping details (output)
-cost (price*quantity rounded off), sales tax, shipping and handling cost, total
-sales tax
    -if ret and town code = 
    -KLA, tax = 10%
    -EBB, MBR = 5%

    if who - tax = 0%
-shipping cost
    -UPS $7
    -US Postal Air $8.5
    -Fedex Ground $9.25
    -Fedex Overnight $12
Total
    -cost + sales_tax + shipping
'''
import math
import pandas as pd
import xlrd
from xlwt import Workbook

class Customer:
    #Customer(customerName, customerID, townCode, customerType): how can a constructor be used?
    def __init__(self): #customerName, customerID, townCode, customerType
        self.customerName = input('Enter customer name: ')
        self.customerID = int(input('Enter customer ID: '))
        self.townCode = int(input('Enter customer location: \n' +
                        '***KEY***\n' +
                        '1: KLA\n' + 
                        '2: EBB\n' +
                        '3: MBR\n'))
        self.customerType = int(input('Enter customer type:\n' + 
                             '***KEY***\n' + '1: retail\n' + '2: wholesale\n'))
    # def getTownCode(self):
    #     return self.townCode
    
    # def getCustomerType(self):
    #     return self.customerType
    
    def salesTax(self, customerType, townCode):
        if (self.customerType == 1):
            if (self.townCode == 1):
                return 0.1
            elif (self.townCode == 2): #add option for 3
                return 0.05
        elif(self.customerType == 2):
            
            return 0.0


class PartOrder:
    def __init__(self): # partNumber, description, partPrice, quantity, oversizeOrderStatus
        self.partNumber = input('Part Number: ')
        self.description = input('Part description: ')
        self.partPrice = int(input('Part price: '))
        self.quantity = int(input('Quantity Ordered: '))
        self.oversizeOrderStatus = int(input('Oversize order quantity: '))
            
    def partPrice(self):
        #partPrice = float(input('Part price: '))
        return self.partPrice
    
    def quantity(self):
        return self.quantity
    
    def cost(self):
        finalCost = math.floor(self.partPrice * self.quantity)
        return finalCost
    '''
    def cost(self, partPrice, quantity):
        price = self.partPrice() 
        quantity = self.quantity()
        finalCost = math.floor(price * quantity)
        return finalCost
        '''
        
customer = Customer()
#customer.customerDetails()
type = customer.customerType #customer.getCustomerType()
code = customer.townCode


newPart = PartOrder()
#newPart.partDetails()
price = newPart.partPrice
quantity = newPart.quantity
cost = newPart.cost()

tax = customer.salesTax(type, code) * cost
#cost = newPart.cost(price, quantity)


shippingMethod = int(input('Enter shipping method of choice from \n' + 
                       '1: UPS\n' +
                       '2: US Postal Air\n' +
                       '3: Fedex Ground\n' +
                       '4: Fedex Overnight: \n'))

def shippingHandling(shippingMethod):
    if (shippingMethod == 1):
        return 7
    elif (shippingMethod == 2):
        return 8.5
    elif (shippingMethod == 3):
        return 9.25
    elif (shippingMethod == 4):
        return 12
    else:
        print('Invalid shipping method')

def printShipMethod(shippingMethod):
    if (shippingMethod == 1):
        return 'UPS'
    elif (shippingMethod == 2):
        return 'US Postal Air'
    elif (shippingMethod == 3):
        return 'Fedex Ground'
    elif (shippingMethod == 4):
        return 'Fedex Overnight'

dollar_rate = 3850

shipping = shippingHandling(shippingMethod) * dollar_rate

def totalBill():
    return float(cost + tax + shipping)
# def partOrder():




def printOutput():
    
    print('\n')
    """ with open('order.txt', 'a') as order:
        order.write(f'Cost = {cost}')
        order.write(f'Sales Tax = {tax}')
        order.write(f'Shipping and Handling = {shipping}')
        order.write(f'Total = {totalBill}')
        
    order.open('order.txt','r') """
    row = 0
    # creat an excel file to save the ordered items and their cost
    ordered = Workbook()
    sheet1 = ordered.add_sheet('Cart')
    sheet1.write(0, 0, 'Part Number')
    sheet1.write(1, 0, 'Product Price')
    sheet1.write(2, 0, 'Tax')
    sheet1.write(3, 0, 'Shipping & Handling')
    #sheet1.write(4, 0, 'Shipping Method')

    row = 1
    #loop_val = range(4)
    # for order in orders:
    sheet1.write(0, 1, newPart.partNumber)
    sheet1.write(1, 1, "{:,}".format(cost))
    sheet1.write(2, 1, "{:,}".format(tax))
    sheet1.write(3, 1, "{:,}".format(shipping))
    #sheet1.write(4, 1, printShipMethod())
    #row += 1
    ordered.save('Cart.xls')
    # print the receipt to the terminal
    print('=======================================')
    print('            PK AUTO GARAGE')
    print('     256 BWAISE NO FLOODS, Uganda')
    print('=======================================')
    print('            Order Details')
    # Using pandas to read the Cart excel file and print to terminal
    print(pd.read_excel('Cart.xls'))
    print('=======================================')
    # printing the total bill
    print(f'                          Total')
    print(f'   UGX              {"{:,}".format(totalBill())} ')
    print('========================================')
    print('')
    print(f'Thanks {customer.customerName} for shopping with us today!')
    print('')
printOutput()