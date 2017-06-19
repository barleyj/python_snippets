

def bind(value, fun):
    def run(config):
        val = value(config)
        return fun(val)
    return run


def read(config_key):
    def run(config):
        return config[config_key]
    return run


def print_list(some_list):
    def run(max):
        return some_list[0:max]
    return bind(read('max'), run)


def t(some_list):
    return some_list[0:max]


def m(**kwargs):
    def run(kwargs):
        print max
    return run
