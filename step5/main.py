def square_digits(num):
    carre = ''
    for i in str(num):
     y = int(i)**2
     carre += str(y)
    return int(carre)