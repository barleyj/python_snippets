from collections import namedtuple


Config = namedtuple('Config', 'max')


def bind(value, fun):
    def run(config):
        val = value(config)
        return fun(val)(config)
    return run


def read(config_key):
    def run(config):
        return getattr(config, config_key)
    return run


def print_list(some_list):
    def run(max):
        for x in some_list[0:max]:
            print x
        return None
    return bind(read('max'), run)
