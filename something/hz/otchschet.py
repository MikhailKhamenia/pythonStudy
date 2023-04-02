import time

def heavy(n):
    for x in range(1, n):
        for y in range(1, n):
            x**y

def sequential(n):
    for i in range(n):
        heavy(10000000000)
    print(f"{n} циклов вычислений закончены")

if __name__ == "__main__":
    start = time.time()
    sequential(80)
    end = time.time()
    print("Общее время работы: ", end - start)