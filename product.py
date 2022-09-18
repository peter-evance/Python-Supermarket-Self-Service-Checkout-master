product_list = [
            {
                'name': 'Avocado',
                'price': 80,
                'description': 'Organic',
                'bar_code': "1"                  
                },
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
            {
                'name': 'File',
                'price': 25,
                'description': 'Organic',
                'bar_code': "5"                  
                },
            {
                'name': 'Banana',
                'price': 25,
                'description': 'Organic',
                'bar_code': "6"                  
                },
            {
                'name': 'Colgate',
                'price': 25,
                'description': 'Organic',
                'bar_code': "7"                  
                },
            {
                'name': 'Peach',
                'price': 25,
                'description': 'Organic',
                'bar_code': "8"                  
                },
            {
                'name': 'Lotion',
                'price': 25,
                'description': 'Organic',
                'bar_code': "9"                  
                },
            {
                'name': 'Wheat Flour',
                'price': 25,
                'description': 'Organic',
                'bar_code': "10"                  
                },
            {
                'name': 'Yoghurt',
                'price': 25,
                'description': 'Organic',
                'bar_code': "11"                  
                },
            {
                'name': 'Apple cider juice',
                'price': 25,
                'description': 'Organic',
                'bar_code': "12"                  
                },
            {
                'name': 'Vineager',
                'price': 25,
                'description': 'Organic',
                'bar_code': "13"                  
                },
            {
                'name': '1kg Meat',
                'price': 25,
                'description': 'Organic',
                'bar_code': "14"                  
                },
            {
                'name': 'Chicken',
                'price': 25,
                'description': 'Organic',
                'bar_code': "15"                  
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

        
