def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, cash):
    cc_pet_shop["admin"]["total_cash"] += cash
    
def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, sold):
    cc_pet_shop["admin"]["pets_sold"] += sold

def get_stock_count(cc_pet_shop): 
    return len(cc_pet_shop["pets"])

# def get_pets_by_breed(cc_pet_shop, breed):
#     specific_breed = []
#     for breed in cc_pet_shop:
#         if breed(len["pets"]["breed"]) == breed:
#             specific_breed.append(breed)
#     return specific_bread

# def gets_pets_by_breed(cc_pet_shop, breed):
#     for specific_breed in cc_pet_shop["pets"]["breed"] == breed:
#         return breed

# def find_pet_by_name(cc_pet_shop, pet_name):
#     for pet in cc_pet_shop:
#         if cc_pet_shop["pets"]["name"] == pet_name:
#             return pet_name
#     return None

def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)