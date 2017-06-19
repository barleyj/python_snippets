from Queue import Queue
from threading import Thread, Lock


class Process():

    def __init__(self):
        self.queue = Queue(10)
        self.lock = Lock()
        s = self._send()
        s.next()
        self.send = s.send

    def __call__(self, *args):
        self.queue.put(args)

    def handle(self, *args):
        pass

    def loop(self):
        queue = self.queue
        while True:
            value = queue.get()
            self.handle(*value)
            queue.task_done()


class IoProcess():

    def __init__(self):
        self.queue = Queue(10)
        threads = []
        for i in range(2):
            t = Thread(target=self.loop)
            t.daemon = True
            t.start()
            threads.append(t)
        self.threads = threads

    def __del__(self):
        self.join()

    def __call__(self, *args):
        self.queue.put(args)

    def handle(self, *args):
        pass

    def loop(self):
        queue = self.queue
        while True:
            value = queue.get()
            self.handle(*value)
            queue.task_done()

    def join(self):
        self.queue.join()
        for t in self.threads:
            t.join(1)


class PTest(Process):
    def __init__(self):
        Process.__init__(self)

    def handle(self, t, x):
        print('P_Test: {0}'.format(t))


class ITest(IoProcess):
    def __init__(self):
        self.p = PTest()
        IoProcess.__init__(self)

    def handle(self, t, x):
        self.p(t, x)

#     def p(self, t, x):
#         print('ITest: {0}'.format(t))

if __name__ == '__main__':
    p = ITest()
    for x in range(5):
        p(x, x * 2)
    p.join()
