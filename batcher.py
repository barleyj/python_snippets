from itertools import islice


MAX_SIZE = 10000


def batch(position=0, size=MAX_SIZE):
    def batched(fun):
        def run(*args):
            arguments = list(args)
            list_to_batch = arguments[position]
            for i in range(0, len(list_to_batch), size):
                slice = islice(list_to_batch, i, i+size)
                arguments[position] = slice
                fun_arguments = tuple(arguments)
                fun(*fun_arguments)
        return run
    return batched
