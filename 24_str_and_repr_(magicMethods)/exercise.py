class Store:
    def __init__( self,name):
        self.name = name# You'll need 'name' as an argument to this method.
        self.items = []# Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):

        create_store = {"name" : name, "price": price}
        self.items.append(create_store)# Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        return sum([create_store["price"] for create_store in self.items])# Add together all item prices in self.items and return the total.
