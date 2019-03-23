import collections
from pprint import pprint
import multiprocessing

import time

import os

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = {
    Scientist(name='Morbus Borbus', field='CS', born=1979, nobel=True),
    Scientist(name='Yana Borbus', field='Chemistry', born=1983, nobel=True),
    Scientist(name='Alex Gulbit', field='Math', born=1979, nobel=True),
    Scientist(name='Dina Gulbit', field='Phy', born=1979, nobel=True),
    Scientist(name='Tata Borbus', field='Social', born=1979, nobel=True),
    Scientist(name='Janna Borbus', field='N/A', born=1979, nobel=True),
    Scientist(name='Vova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='Troy Borbus', field='Happy', born=1979, nobel=True),
    Scientist(name='Vova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='AVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='BVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='CVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='DVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='FVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='EVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='WVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='QVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='RVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='RRVova Borbus', field='Medicine', born=1979, nobel=True),
    Scientist(name='ZVova Borbus', field='Medicine', born=1979, nobel=True)
}


def transform(x):
    print(f'Processing record {x.name}' + "process running job is : " f'{os.getpid()}')
    time.sleep(1)
    transformation_result = {'name': x.name, 'age': 2017 - x.born}
    print(f'Done processing record {x.name}')
    return transformation_result


if __name__ == "__main__":
    pprint(scientists)
    start = time.time()
    # decide later which one is better
    # pool = multiprocessing.Pool() # python is making decision regarding number of processes based on CPU spec?
    # so far this is the faster variant on a single file
    pool = multiprocessing.Pool(processes=len(scientists))  # I define separate process for each line

    # pool = multiprocessing.Pool(processes=int(len(scientists) / 4),
    #                             maxtasksperchild=1)  # I define to restart process once it is complete

    result = pool.map(transform, scientists)
    end = time.time()
    print(f'Time to complete: {end - start:.2f}')
    # pprint(result)

    print("Now single_process for comparison \n")
    start = time.time()

    mapped_result = tuple(map(
        transform,
        scientists
    ))
    end = time.time()
    print(f'Time to complete: {end - start:.2f}')