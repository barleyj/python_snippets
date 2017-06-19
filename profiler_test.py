import cProfile


class profiler:
    def __init__(self, profiler=None):
        self.pr = profiler
    def __enter__(self):
        if self.pr:
            self.pr.enable()
    def __exit__(self, type, value, traceback):
        if self.pr:
            self.pr.disable()


with profiler(cProfile.Profile()):
    print('blah')
