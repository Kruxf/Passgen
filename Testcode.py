import random
while True:
    #main program
    while True:


        a = 'abcdefghijklmnopqrstuvwxyz'
        n = '0123456789'
        g = '!@#$%&*+?'
        word = ['Absol', 'Beedrill', 'Charmander', 'Deoxys', 'Eevee', 'Feebas', 'Geodude', 'Happiny', 'Ivysaur', 'Jynx', 'Kabuto', 'Lapras',
                'Magikarp', 'Natu', 'Oddish', 'Paras', 'Qwilfish', 'Ralts', 'Suicune', 'Tauros', 'Unown', 'Voltorb', 'Weezing', 'Xatu', 'Yanma', 'Zapdos']
        greet = ['Have a nice day!', 'Goodbye.', 'See Ya!',
                 'Aloha', 'Ciao!', 'Sayonara!', 'Hasta la vista baby!', 'Shutting down...']

        an = 4  # alpha number
        nn = 3  # alphanumeric number
        gn = 3  # gramatical number
    #cpl = 10  # complete password

        rn = ''.join(random.sample(n, nn))
        rg = ''.join(random.sample(g, gn))
        ra = ''.join(random.sample(a, an))
        oa = (random.choice(n))
        rw = (random.choice(word))

        low = (rw+oa)
        med = (rw+rg+oa)
        high = (rn+rw+oa+rg)
        grt = (random.choice(greet))

        strength = input('\n Please select desired password strength\n \n (1) Low \n (2) Medium \n (3) High\n\n  ')


        if strength == '1':
            print(low)

        elif strength == '2':
            print(med)

        elif strength == '3':
            print(high)

        if strength in ('1', '2', '3'):
            break
        else:
            print(' Invalid Input, Please try again.\n')
            continue

    while True:
        answer = input('Would you like to create another password? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print(grt)
        break
