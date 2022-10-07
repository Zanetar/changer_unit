def high():
    try:
        while True:
            print('Dokonaj wyboru')
            print('1. Zamiana mm/cm ')
            print('2. Zamiana cm/m')
            print('3. Zamiana mm/m')
            print('4. Zamiana m/mm ')
            print('5. Zamiana m/cm')
            print('6. Zamiana cm/mm')
            print('x. -Wyjście')
            choice =input('Dokonaj wyboru')
            choice.upper()
            if choice == 'X':
                print('Do widzenia')
                break
            else:
                choice = int(choice)
                if choice == 1:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f"{value}mm. to {value / 10} cm")
                elif choice == 2:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}cm. to {value / 100} m')
                elif choice == 3:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}mm. to {value / 1000} m')
                elif choice == 4:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}m. to {value * 1000} mm')
                elif choice == 5:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f"{value}m. to {value * 100} cm")
                elif choice == 6:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}cm. to {value * 10} mm')
                else:
                    print('Wybrałeś zły znak')
    except: print('Wybrłeś zły znak!')



def liquid():
    try:
        while True:
            print('Dokonaj wyboru')
            print('1.Zamiana ml/l ')
            print('2. Zamiana l/ml')
            print('x -wyjście')
            choice = input('Dokonaj wyboru').upper()
            if choice == 'X':
                print('Do widzenia')
                break
            else:
                choice = int(choice)
                if choice == 1:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}ml. to {value / 1000} l')
                elif choice == 2:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}l. to {value * 1000} ml')
                else:
                    print('Wybrałeś zły znak')
    except: print('Wybrłeś zły znak!')


def weight():
    try:
        while True:
            print('Dokonaj wyboru')
            print('1. Zamiana g/kg ')
            print('2. Zamiana kg/t')
            print('3. Zamiana g/t')
            print('4. Zamiana t/g ')
            print('5. Zamiana t/kg')
            print('6. Zamiana kg/g')
            print('x. -wyjście')
            choice = input('Dokonaj wyboru').upper()
            if choice == 'x':
                print('Do widzenia')
                break
            else:
                choice = int(choice)
                if choice == 1:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}g. to {value / 1000} kg')
                elif choice == 2:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}kg. to {value / 1000}t')
                elif choice == 3:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}g. to {value / 100000} t')
                elif choice == 4:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}t. to {value * 1000000} g')
                elif choice == 5:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f"{value}t. to {value * 1000} kg")
                elif choice == 6:
                    value = float(input('Wpisz wartość jaką chcesz zamienić'))
                    print(f'{value}kg. to {value * 1000} g')
                else:
                    print('Wybrałeś zły znak')
    except:
        print('Wybrłeś zły znak!')

def menu():
    try:
        while True:
            print('Witaj w kalkulatorze jednostek')
            print('Co chcesz zrobić?')
            print('1. Zamiana jednostek długości')
            print('2. Zamiana jednostek objętości ')
            print('3. Zamiana jednostek masy')
            print('x. Wyjście')
            choice=input('Dokonaj wyboru').upper()
            if choice=='X':
                print('Do widzenia')
                break
            else:
                choice=int(choice)
                if choice==1:
                    high()
                elif choice==2:
                    liquid()
                elif choice==3:
                    weight()
                else:
                    print('Wybrałeś zły znak! Do widzenia')
                    break
    except: print('Wybrałeś zły znak! Do widzenia!')

menu() #wywołanie programu
