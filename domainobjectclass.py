import json


class DomainObjectClass:
    """
    Parent class of PEST 
    """
    id = None
    name = None
    title = None
    description = None
    data = None

    def __init__(self, id=None, name=None, title=None, description=None, data=None, json_data=None):
        """
        Initializes the DomainObjectClass
        """
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.data = data
        self.json_data = json_data

    @classmethod
    def object_from_json(cls, json_data):
        """
        function which converts json to object
        :return:
        """
        data_object = json.loads(json_data)
        id = data_object['id']
        name = data_object['name']
        title = data_object['title']
        description = data_object['description']
        data = data_object['data']

        return cls(id, name, title, description, data, data_object)


test = DomainObjectClass(id=1, name='anu', title='x', description='y', data='z')
print(test.id)

