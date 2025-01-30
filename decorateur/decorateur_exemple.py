import time

def benchmark(fonction):
    def wrapper(*args, **kwargs):
        begin = time.time()
        fonction(*args, **kwargs)
        end = time.time()
        print(f"{fonction.__name__} : {end - begin} seconds")
    return wrapper

@benchmark
def fonction_a():
    time.sleep(1)
    print("Je suis dans la fonction a")

@benchmark
def fonction_b():
    time.sleep(2)
    print("Je suis dans la fonction b")

fonction_a()

fonction_b()