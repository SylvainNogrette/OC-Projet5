def log_decorator(func):
    def wrapper():
        print("Ce message s'affiche avant la fonction décorée")
        func()
        print("Ce message s'affiche après la fonction décorée")
        return
    return wrapper

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")
    return

function_test()
