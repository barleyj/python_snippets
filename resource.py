import json
from json import JSONEncoder


class ResourceEncoder(JSONEncoder):
    def default(self, o):
        return {'apiVersion': 'extensions/v1beta1',
                'kind': 'ThirdPartyResource',
                'metadata': {'name': '.'.join([o.name.lower(), o.namespace])},
                'description': o.description,
                'versions': {'name': o.version},
                }


class Resource:
    version = 'v1'
    description = "Some description"
    
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        self.namespace = __name__



j = json.dumps(Resource(), cls=ResourceEncoder)
print(j)

