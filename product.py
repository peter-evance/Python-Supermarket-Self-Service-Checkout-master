product_list = [
            {
                'name': 'Pen',
                'price': 25,
                'description': 'Organic',
                'bar_code': "2"                  
                },
            {
                'name': 'Pencil',
                'price': 25,
                'description': 'Organic',
                'bar_code': "3"                  
                },
            {
                'name': 'Clipboard',
                'price': 25,
                'description': 'Organic',
                'bar_code': "4"                  
                },
        ]   

class Product():
    """Represent product object in the supermarket inventory.
    Class atrributes such as the name,price, description describes the product particulars."""
    
    def __init__(self,name,price,description,bar_code):
        """Initializes the particulars(attributes) of a product"""
        
        self.name = name
        self.price = price
        self.description = description
        self.bar_code = bar_code
        
    def check_product_on_inventory(self):
        """Function : Queries the availabilty of a particular product in the product list
        Return Value: Returns a True/False(Boolean value) thus flaggging availability of a particular product."""
        
        found = False       
        for index, product in enumerate(product_list):  
            if self.bar_code == product['bar_code']:                
                product_found = {'name': product['name'],
                                 'price': product['price'],
                                 'description': product['description'],
                                 'bar_code': product['bar_code']}
                found = True
                print(product['name']," -  $"+str(product['price']),'\n' )     
        if found == True :            
            return product_found
        else:
            return False

        
