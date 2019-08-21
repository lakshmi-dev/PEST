import json

from DI.PEST.dimension import Dimension
from DI.PEST.domainobjectclass import DomainObjectClass


class PEST(DomainObjectClass):
    """
    framework level class
    """
    dimensions = None

    def generate_graph(self):
        pass


pest_trial = PEST(id=1, name='anu', title='x', description='y', data='z')
print(pest_trial.data)
print(pest_trial.title)




