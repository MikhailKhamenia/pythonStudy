class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

rect = Rectangle(5, 6)
print(rect.area)


import time


def retry(max_retries):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except:
                    time.sleep(1)
        return _wrapper
    return retry_decorator


@retry(2)
def might_fail():
    print("might_fail")
    raise Exception


might_fail()

