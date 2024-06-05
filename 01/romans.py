def int_to_roman(num):
    # Implemente sua função aqui    
    valores = (
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    )

    resultado = ""
    for valor, romano in valores:
        while num >= valor:
            resultado += romano 
            num -= valor
    return resultado



def roman_to_int(s):
    # Implemente sua função aqui
    valores = { 
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100, 
        'XC': 90,
        'L': 50, 
        'XL': 40,
        'X': 10, 
        'IX': 9, 
        'V': 5, 
        'IV': 4,
        'I': 1
    }
    i = 0
    total = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in valores:
            total += valores[s[i:i+2]]
            i +=2
        else:
            total += valores[s[i]]
            i += 1
    return total 

num = int(input("Digitar Número: "))
print (int_to_roman(num))
s = (input("Digitar Número Romano: "))
print (roman_to_int(s))
