
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    
    for _ in list(range(num_products)):
        product_name = sample(ADJECTIVES,k=1)+sample(NOUNS,k=1)
        product = Product(name = ' '.join(product_name),
                          price=randint(5,100), weight=randint(5,100),
                          flammability=uniform(0.0,2.6))
                          #I chose 2.6 because uniform is exclusive
                       
        products.append(product)
    
    return products


def inventory_report(products):
    '''Print out a product report given a list of products

    Parameters
    -----------------------------
    products : list
        a list of Product class instances
    '''
    total_price = 0
    total_weight = 0
    total_flammability = 0

    unique_names = set()
    for product in products:
        unique_names.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability
    
    average_price = total_price/len(products)
    average_weight = total_weight/len(products)
    average_flammability = total_flammability/len(products)

    print('\n---ACME CORPORATION OFFICIAL INVENTORY REPORT---')
    print('Unique product names:',len(unique_names))
    print('Average price:',round(average_price,2))
    print('Average weight:',round(average_weight,2))
    print('Average flammability rating:',round(average_flammability,2))


if __name__ == '__main__':
    inventory_report(generate_products())