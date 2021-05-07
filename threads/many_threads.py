"""An example showing how to use ThreadPoolExecutor"""

from concurrent.futures import ThreadPoolExecutor

some_dummy_data = ('foo', 'bar', 'buzz')


def mapper(data):
    return data.upper()


def hello(name):
    print(f"hello from thread {name}!")


with ThreadPoolExecutor(max_workers=3) as pool:
    # res = pool.map(mapper, some_dummy_data)
    for name in ('a', 'b', 'c'):
        pool.submit(hello, name)
