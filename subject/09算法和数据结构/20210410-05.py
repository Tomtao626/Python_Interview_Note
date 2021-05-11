from functools import wraps
import time


def metric(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        tims = ((end - begin) * 1000)
        print('%s executed in %s ms' % (func.__name__, tims))

    return wrapper


# 测试
@metric
def testA(x, y):
    time.sleep(0.5)
    return x + y


@metric
def testB(x, y, z):
    time.sleep(1)
    return x * y * z


testA(11, 22)  # testA executed in 504.03809547424316 ms
testB(11, 22, 33)  # testB executed in 1000.4549026489258 ms
