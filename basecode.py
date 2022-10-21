pizzas = ['Regular', 'Whole wheat']
toppings = ['Mozzarella cheese', 'Cheddar cheese', 'Spinach', 'Corn', 'Mushroom', 'Chicken', 'Pepperoni']
sauces = ['Marinara sauce', 'Pesto sauce']
p_price = {"Regular":50, "Whole wheat":75}
t_price = {'Mozzarella cheese':30, 'Cheddar cheese':35,
 'Spinach':20, 'Corn':15, 'Mushroom':15, 'Chicken':50, 
 'Pepperoni':45}
drinks = ['Pepsi', '7-up', 'Coke']
dessert = ['Lava Cake', 'Chocholate brownie']
dr_price = {'Pepsi':17, '7-up':19, 'Coke':20}
ds_price = {'Lava Cake':95, 'Chocolate brownie':86}

total = 0
flag = 0
summarypizza = []
summaryprice = []
summarysauce = []
summarytopping = []
summaryextra = []

def Menu():
    print(f"Available pizzas : {pizzas}")
    print(f"Sauces: {sauces}")
    print(f"Toppings: {toppings}")

def TakeOrder(total):
    print('Hi, Welcome to the Pizza Delivery!')
    ordering = True
    while ordering:
        Menu()
        p = input('Please choose a pizza: ') 
        if p not in pizzas:
            print(f"Sorry, we don't have {p}.")
            TakeOrder()
        else:
            print(f"You have ordered {p}.")
            print(f"{p} will have a price of {p_price[p]}.")
            total += p_price[p]
            summarypizza.append(p)
            summaryprice.append(p_price[p])


        s = input('Choose sauce: ')
        if s not in sauces:
            print(f"We don't have {s}.")
        else:
            print(f"You have ordered {s}.")
            summarysauce.append(s)
            Toppings(total)


def Toppings(total):
    t = input('Please choose topping:  ')
    if t not in toppings:
        print(f"Sorry, we don't have {t}.")
    else:
        print(f"You have ordered {t}.")
        print(f"{t} will have a price of {t_price[t]}.")
        total += t_price[t]
        summarytopping.append(t)
        summaryprice.append(t_price[t])
    
    choice = input('Would you like to have another topping?(yes/no) ')
    if choice == 'yes':
        Toppings(total)
    elif choice == 'no':
        d = input('Would you like to order  drinks or dessert? yes/no   ')
        if d == 'yes':
            print('Yay! you will have a discount of 5%.')
            DrinkDessert(total, flag)
        elif d == 'no':
            CalculatePrice(total)
        else:
            print("Sorry, we don't understand you. ")
        

def DrinkDessert(total, flag):          
    ext = input('Enter drinks/dessert: ')
    flag = 1
    if ext == 'drinks':
        print(f'You have ordered {ext}. ')
        print(f"Drinks: {drinks}")
        d = input('Which drink do you want? ')
        if d in drinks:
            print(f"{d} will have a price of {dr_price[d]}  ")
            total += dr_price[d]
            summaryextra.append(d)

    elif ext == 'dessert':
        print(f'You have ordered {ext}. ')
        print(f"Dessert: {dessert}")
        d = input('Which dessert do you want? ')
        if d in dessert:
            print(f"{d} will have a price of {ds_price[d]}  ")
            total += ds_price[d]

    ex = input('Would you like another drink/dessert?(press yes/no) ')
    if ex == 'yes':
        DrinkDessert(total, flag)
    elif ex == 'no':
        CalculatePrice(total)
    else:
        print("Sorry, we don't understand you :/")


def CalculatePrice(total):
    if flag == 1:
        total = 0.95 * total
    else:
        return total

def OrderSummary(summarypizza, summaryprice, summarysauce, summarytopping, summaryextra):
    print(f"Pizza Base: {summarypizza}")
    print(f"Sauce: {summarysauce}")
    print(f"Topping: {summarytopping}")



if __name__ == "__main__":
    TakeOrder(total)
    OrderSummary(summarypizza, summaryprice, summarysauce, summarytopping, summaryextra)
    CalculatePrice(total)
