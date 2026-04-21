def calculate_square(number):
    try :
        return number ** 2
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None

print(str(calculate_square(5)))
print(str(calculate_square(2.1)))
print(calculate_square("Arnaud"))
