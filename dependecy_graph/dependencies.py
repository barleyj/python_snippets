from math import ceil

from pygraphviz import *


def get_shards(message_count, message_size, reader_count):
    MB = (1024 * 1024)
    write_shards = (message_count * message_size * 1.0) / MB
    read_shards = (reader_count * message_count * message_size * 1.0) / (MB * 2)
    return max(int(ceil(write_shards)), int(ceil(read_shards)))


dependencies = AGraph()


class DependencyMeta(type):
    def __new__(cls, name, parents, dct):
        # if 'count' not in dct:
        #     dct['count'] = 1

        if 'name' not in dct:
            dct['name'] = name

        if 'dependencies' not in dct:
            dct['dependencies'] = []

        for dep in dct['dependencies']:
            dependencies.add_edge(dct['name'], dep.name)
            if 'shape' in dir(dep):
                node = dependencies.get_node(dep.name)
                node.attr['shape'] = dep.shape


        return super(DependencyMeta, cls).__new__(cls, name, parents, dct)


class Service(object):
    __metaclass__ = DependencyMeta


class DataStore(Service):
    shape = 'house'


class Stream(Service):
    shape = 'triangle'


class ElasticSearch(Service):
    name = 'Elastic Search'


class S3(DataStore):
    name = 'S3'


class Presto(Service):
    dependencies = [ElasticSearch, S3]


class Transform(Service):
    # name = 'AWS Lambda'
    dependencies = [S3]


class KinesisFirehose(Service):
    name = 'Kinesis Firehose'
    dependencies = [S3]


class KinesisStreams(Stream):
    name = 'Kinesis Streams'
    dependencies = [ElasticSearch, Transform, KinesisFirehose]


class Ingress(Service):
    name = 'Ingress API'
    dependencies = [KinesisStreams]


class Kafka(Stream):
    dependencies = [Ingress]


class Core(Service):
    dependencies = [Kafka]


dependencies.layout(prog='dot')
dependencies.draw('file.png')
