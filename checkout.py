class Checkout():
    """Extends the queries and functionalities of products by use of helper functions"""
    def __init__(self,checkout_date,checkout_items):
        self.checkout_date = checkout_date
        self.checkout_items = checkout_items

    def calculate_payment_due(self):
        """ Function : Aggregates the total payment that is required for the purchase
            Returns  : Calculated sum plus the tax region factored in."""
            
        tax = str(input("\n Please enter tax area (N)airobi or (K)isumu ?: "))
        cart_totals = 0
        for index, product in enumerate(self.checkout_items):
            if tax.lower() == "n":
                cart_totals += (product['price'])*1.06
            elif tax.lower() == "k":
                cart_totals += (product['price'])*1.05
            else:
                cart_totals += product['price']         
        self.due = cart_totals
        return cart_totals

    def pay_money(self,total):
        amount_to_pay = total
        print("\nPayment due: $"+str(amount_to_pay))
        change = self.accept_payment(amount_to_pay)
        return change
        

    def accept_payment(self, amount_to_pay):
        """Function : Evaluates and accepts a valid payment
           Returns :  Validated payment and change if need be."""

        paid = float(0.0)
        customer_pay = float(0.0)
        due = float(0.0)
        total = amount_to_pay
        due = True
        
        while due == True:
            try:
                paid = float(input("\nPlease enter an amount to pay: "))
                if(paid < 0.0):
                    print("Incorrect value, Re-enter amount!\n")
                    continue
                else:
                    customer_pay += paid
                    self.customer_pay = round(customer_pay,2)
                    if(paid < total):
                        due = total - paid
                        total = due
                        print("Payment due: $"+str(due))      
                        due = True
                        continue   
                    else:
                        change = paid - total
                        self.change = change
                        return change                
            except ValueError:
                print('Please enter a valid currency value.')
        return change
                        
    def print_receipt(self,change):
        """Defines the structure and arrangement of console out receipt"""
        
        print("\n------------- Final Receipt -----------\n")
        print("            "+self.checkout_date,"\n")
        print("ITEM                     AMOUNT")
        print("-----------------------------------------")

        for index, item in enumerate(self.checkout_items):
            print(item['name'],'           $'+str(item['price']))

        print("-----------------------------------------")
        print("Total amount due:",'     $'+str(self.due))
        print("Amount Received",'       $'+str(self.customer_pay))
        print("Change Given",'          $'+str(self.change))
        


    
        
        
        
        
        
                        
                        
                

        
            
            
        
        
   
