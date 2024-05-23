from collections import defaultdict
class Shopping_Cart:
    sname = 'Lucky Icare'
    sloc = 'Rasulgarh'
    stock = {
        'iphone 13': 15,
        'iphone 13 plus': 10,
        'iphone 13 promax': 5,
        'iphone 14': 15,
        'iphone 14 plus': 10,
        'iphone 14 promax': 5,
        'iphone 15': 15,
        'iphone 15 plus': 10,
        'iphone 15 promax': 5,
        }

    prices = {
        'iphone 13': 60000,
        'iphone 13 plus': 90000,
        'iphone 13 promax': 129999,
        'iphone 14': 70000,
        'iphone 14 plus': 99999,
        'iphone 14 promax': 149999,
        'iphone 15': 79999,
        'iphone 15 plus': 139999,
        'iphone 15 promax': 169999,
        }

    def __init__(self, name, pno, email,add):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.cart = defaultdict(int)

    def add_item(self, item, count=1):
        if item in self.stock:
            if self.stock[item] >= count:
                self.cart[item] += count
                Shopping_Cart.stock[item] -= count
                print('Item Added to Cart Successfully')
            else:
                print(f'The {item} has no required amount of stock')
                print(f" We have only {self.stock[item]} pieces {item}")
        else:
            print(f"Sorry We dont sell {item}")

    def remove_item(self, item, count=1):
        if item in self.cart:
            if self.cart[item] >= count:
                self.cart[item] -= count
                Shopping_Cart.stock[item] += count
                if self.cart[item] == 0:
                    self.cart.pop(item)
                print('Item has been Removed from the Cart Successfully')
            else:
                print(f'The {item} has no required count in cart')
                print(f" you have only {self.cart[item]} pieces {item}")
        else:
            print(f"you dont have {item} in your cart")

    def display_cart(self):
        total = 0
        for item,count in self.cart.items():
            price = self.prices[item]
            print(f"The {item} is rupees {price} and you added {count} total is {price*count}")
            total += count*price
        print(f"The Grand total is :{total} onlyyyy....:)")

    def checkout(self):
        self.display_cart()
        print('Press 1 to confirm')
        print('Press 0 to Continue Shopping')
        conf = int(input('enter the Response'))
        if conf:
            self.cart.clear()
            print('Order Placed Successfully')
            print('Thanks for Shopping With Us  Visit Again With Your Friend"s Kidney')
c1 = Shopping_Cart('steve', 8179267926, 'steve@gmail.com', 'Bhubaneshwar')
