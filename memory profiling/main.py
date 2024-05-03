from memory_profiler import profile, memory_usage

# log_file = open('memory.log', 'w+')


@profile
def myfunction(list_size):
    mylist = ['hello'] * list_size
    mylist2 = ['world'] * list_size
    del mylist2
    return mylist


myfunction(100000)
myfunction(1000000)
myfunction(10000000)

# mem_usage = memory_usage((myfunction, (), {'list_size': 100000}), max_usage=True)
# print(mem_usage)
