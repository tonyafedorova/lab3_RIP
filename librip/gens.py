import random


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for x in items:
            for a in args:
                yield x[a]
    else:
        for x in items:
            for a in args:
                if x[a] is not None:
                    yield {a: x[a]}
    # реализовала генератор


def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield random.randint(begin, end)
    # Реализовала генератор
