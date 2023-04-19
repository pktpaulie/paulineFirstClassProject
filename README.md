# paulineFirstClassProject
First Python Project regarding an auto store.


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
