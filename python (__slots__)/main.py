import statistics
import timeit

from memory_profiler import memory_usage


class PointWithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def create_points():
    return [PointWithoutSlots(i, i) for i in range(1000000)]


mem_values = []
time_values = []

for _ in range(10):
    mem_usage_without_points = memory_usage(create_points, interval=0.01)
    mem_values.append(max(mem_usage_without_points))

    point = PointWithoutSlots(1, 2)
    time_without_slots = timeit.timeit(lambda: (point.x, point.y), number=1000000)
    time_values.append(time_without_slots)

print(statistics.mean(mem_values))
print(statistics.mean(time_values))
