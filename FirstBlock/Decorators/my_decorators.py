def decorator_function(func):
    def _wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        func()
        print('Выполняем обёрнутую функцию...')

        print('Выходим из обёртки')
    return _wrapper

def decorator_bread(func):
    def _wrapper():
        print('Функция хлебушка')
        func()
    return _wrapper

@decorator_bread
@decorator_function
def hello_world():
    print('Hello world!')

hello_world()

import requests
import time
def benchmark(func):
    def _wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return _wrapper

@benchmark
def fetch_webpage():
    webpage = requests.get('https://google.com')
fetch_webpage()



iters=int(input('Input number:\n'))
def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper
    return actual_decorator


@benchmark(iters)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')
print(webpage)