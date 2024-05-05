def generator():
    yield 1
    yield 2


def other_generator():
    yield "Hello World"

    yield from "Hello World"

    yield "Good Bye"


gen = other_generator()

for value in gen:
    print(value)
