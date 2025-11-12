
class Item():
    def __init__(self,name: str,price: float):
        self.name = name
        self.price = price

class Cart():
    def __init__(self):
        self.items = []
        self.totalPrice = 0

    def show(self):
        for i in range(0,len(self.items)):
            print(f"\n{i+1} ~ {self.items[i].name} ~ £{self.items[i].price}")
    
    def addItem(self,itemToAdd: object):
        self.items.append(itemToAdd)
        print(f"\nYou have added '{itemToAdd.name}' to your cart.\nYour item(s) are now:")
        self.show()
        
    def remItem(self,itemToRem: object):
        if len(self.items) <= 0:
            print("\nYou can not remove an item, your cart is empty!")
        else:
            for i in range(0,len(self.items)+1):
                if self.items[i] == itemToRem:
                    self.items.pop(i)
                    print(f"\nYou have removed '{itemToRem.name}' from your cart.\nYour item(s) are now: ")

                    break
                
    def calcPrice(self,discount: float):
        if discount != None:
            if discount > 0:
                for i in self.items:
                    total += i.price * discount
        else:
            for i in self.items:
                total += i.price
        return total

def main():
    cart_1 = Cart()
    items = [Item("Carrot",0.3),Item("Cucumber",0.45),Item("Watermelon",1.25)]

    while True:

        print("\nThese are the choices of items in the shop:")

        if len(items) > 0:
            for i in range(0,len(items)):
                print(f"\n{i+1}-{items[i].name} ~ {items[i].price}")
        else:
            print("\nStore is now empty.")
        
        choice = int(input("\nWould you like to add (1) or remove (2) an item from your cart? : "))

        if choice == 1:
            choice_2 = int(input("\nWhich number item to add? :"))

            if choice_2 in range(1,len(items)+1):
                cart_1.addItem(items[choice_2-1])
                items.pop(choice_2-1)
            else:
                print("\nItem entered not found in store.")
        elif choice == 2:
            choice_2 = int(input("\nWhich number item to remove? :"))

            if choice_2 in range(1,len(items)+1):
                cart_1.remItem(items[choice_2-1])
                items.append(choice_2-1)

main()


    
