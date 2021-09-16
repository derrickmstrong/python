# def = define function 

def sayHello(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(sayHello('es'), 'Derrick' )
print(sayHello('fr'), 'Malone' )
print(sayHello('en'), 'Mr. Strong' )