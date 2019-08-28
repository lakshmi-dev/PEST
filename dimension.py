
# from DI.PEST.pest import *
from DI.common_modules.domainobjectclass import DomainObjectClass
# from DI.PEST.pest import PEST


class Dimension(DomainObjectClass):
    """
    dimensions of PEST
    """
    parent = None
    factors = None


dim_trial = Dimension(id=1, name='anu', title='x', description='y', data='z')
print(dim_trial.name)


