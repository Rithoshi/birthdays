'''
The goal of the module is to create a dictionary that has as key the name of a VIP and as keys his or her birthday.
After that we create a function that the available VIP and a function that ask in input the name of a VIP and return the birthday'''

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Pietro prova': '01/6/1955'}
#Ciao
def print_birthdays():
    '''This function print the name of VIP inside the dictionary, so the available birthdays. '''
    print('Welcome to the birthday dictionary. These are the birthdays:')
    for name in birthdays:
        print(name)

def return_birthday(name,v):
    '''This function has a name as inpit and return the birthday if available, or an error if not '''
    if name in birthdays:
        if v==False:
            print('{}\'s birthday is {}.'.format(name, birthdays[name]))
        else:
            print(birthdays[name])
    else:
        if v==False:
            print('Noooooooo, we don\'t have {}\'s birthday.'.format(name))
        else:
            print("IDK")
