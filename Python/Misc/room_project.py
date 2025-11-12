from math import pi

################ SUBROUTINES ###################

def calc_rect(item):
    while True:
        try:
            width = float(input(f"\nEnter the width of your {item} in metres: "))
            length = float(input(f"\nEnter the length of your {item} in metres: "))
            if width <= 0 or length <= 0:
                raise ValueError
            break
        except:
            print("\nInvalid Entry")
    return width * length

def calc_tri(item):
    while True:
        try:
            width = float(input(f"\nEnter the width of your {item} in metres: "))
            length = float(input(f"\nEnter the length of your {item} in metres: "))
            if width <= 0 or length <= 0:
                raise ValueError
            break
        except:
            print("\nInvalid Entry")
    return (width * length) / 2

def calc_circ(item):
    while True:
        try:
            diameter = float(input(f"\nEnter the diameter of your {item} in metres: "))
            if diameter <= 0:
                raise ValueError
            break
        except:
            print("\nInvalid Entry")
    return round(pi * ((diameter / 2) ** 2),3)

def calc_totalArea(fl_area,rem_items):
    temp = fl_area
    for i in rem_items:
        temp -= i
    if temp <= 0:
        print("Invalid total carpet area.")
        main()
    else:
        return temp

def get_price(item):
    while True:
        try:
            price = float(input(f"\nEnter the price of your {item} per m²: "))
            if price <= 0:
                raise ValueError
            break
        except:
            print("\nInvalid Entry.")
    return price

def calc_carpCost(area,carp,under,lab):
    if area >= 20:
        print("\nYou qualify for a 15% discount on your carpet and a 5% discount on labour costs.")
        cost = ((area * carp) * 0.85) + ((area * lab) * 0.95) + (area * under)
    else:
        cost = (area * carp) + (area * lab) + (area * under)
    return cost
    
def main():
    fl_area = calc_rect("floor")
    rem_items = [calc_rect("cupboard"),calc_rect("shelf"),calc_tri("tiles"),calc_circ("table")]
    total_area = calc_totalArea(fl_area,rem_items)
    prices = [get_price("carpet"),get_price("underlay"),get_price("labour")]
    total_cost = calc_carpCost(total_area,*prices)

    print(f"\nThe total cost of your carpet is: £{round(total_cost,2)}")
    return
################ MAIN PROGRAM ###################

if __name__ == "__main__":
    main()
