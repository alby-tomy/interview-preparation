
# Method 1
def key_max_value():
    d_items = {}
    
    num_items = int(input(f"Enter the number of items : "))
    for i in range(num_items):
        item_key = input(f"Enter the name of the item {i+1} : ")
        item_value = float(input(f"Enther the price of item {i+1} : "))
        
        d_items[item_key] = item_value
        
    if not d_items:
        print("No items provided")
        return
    
    max_price = max(d_items.values())
    highest_priced_i = [item for item, price in d_items.items() if price == max_price]
    
    print("Items with the highest price : ")
    for item in highest_priced_i:
        print(item)

key_max_value()


# Method 2 
def key_max_value_simple():
    d_items = {}
    
    num_items = int(input("Enter the number of items : "))
    
    for i in range(num_items):
        d_key = input(f"Enter the name of the item {i+1} : ")
        d_val = float(input(f"Enter the value {i+1} : "))
        d_items[d_key] = d_val
        
        
    max_price = 0
    h_price_item = []
    for item, price in d_items.items():
        if price > max_price:
            max_price = price
            h_price_item = [item]
        elif price == max_price:
            h_price_item.append(item)
            
            
    if h_price_item:
        print("Items with the highest price:")
        for item in h_price_item:
            print(item)
    else:
        print("No items provided.")

# Example usage:
key_max_value_simple()