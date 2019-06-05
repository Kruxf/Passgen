import random
print('Please select the desired level of security.')

a = 'abcdefghijklmnopqrstuvwxyz'
n = '0123456789'
g = '!@#$%&*+?'

word = ['Absol', 'Beedrill', 'Charmander', 'Deoxys', 'Eevee', 'Feebas', 'Geodude', 'Happiny', 'Ivysaur', 'Jynx', 'Kabuto', 'Lapras',
        'Magikarp', 'Natu', 'Oddish', 'Paras', 'Qwilfish', 'Ralts', 'Suicune', 'Tauros', 'Unown', 'Voltorb', 'Weezing', 'Xatu', 'Yanma', 'Zapdos']
an = 4
nn = 3
gn = 3
complete = 10

# Random alpha,num,gramatical
rn = ''.join(random.sample(n, nn))
rg = ''.join(random.sample(g, gn))
ra = ''.join(random.sample(a, an))

wp = (random.choice(word))
wpn = (wp + rn)
# WeakPasswords = wpn

mpw = (rg+rn+ra+ra.upper())     # Using
mpc = ''.join(random.sample(mpw, complete))
# MediumPassword = mpc 3.322 bit password

spc = rn+(random.choice(word)+rg)

password = int(input('\n 1. Low \n 2. Average \n 3. High \n'))

if(password == 1):
    print(wpn)
       # int(input('Create another password?'):
        # if(response == 1):
     #       print('Please select the desired level of security.')

elif(password == 2):
    print(mpc)
    #input('Create another password?')

elif(password == 3):
    print(spc)
    #input('Create another password?')