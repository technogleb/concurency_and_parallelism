"""An example showing how to use ThreadPoolExecutor"""

from concurrent.futures import ThreadPoolExecutor

some_dummy_data = ('foo', 'bar', 'buzz')


def mapper(data):
    return data.upper()


with ThreadPoolExecutor(max_workers=3) as pool:
    res = pool.map(mapper, some_dummy_data)
    print(list(res))
