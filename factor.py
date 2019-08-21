

from DI.PEST import DomainObjectClass, pest, dimension


class Factor(DomainObjectClass):
    """
    Factors of dimension
    """

    parent = None


fact_trial = Factor(id=1, name='anu', title='x', description='y', data='z')
# print(fact_trial.name)
print(fact_trial.description)
pst_trial = pest.PEST(id=1, name='anu', title='x', description='y', data='z')
print(pst_trial.name)
dim_trial = dimension.Dimension(id=2, name='Salu', title='m', description='n', data='o')
print(dim_trial.data)
