from DI.PEST.model_pb2 import PNucleus
from DI.PEST.utility import apply

m1 = PNucleus()
m1.id = '1'
m1.suffix = 'test_suffix'
m1.title = 'test_title'
m1.description = 'test_description'
m1.type = 'test_type'
m1.category = 'test_category'
m1.handle = 'test_handle'
# m1.tags = 'test_tag'
m1.created = 'test_created'
print(m1)


serialized = m1.SerializeToString()
print(serialized)
serialized = b'\n\x011\x12\x0btest_suffix\x1a\ntest_title"\x10test_description*\ttest_type2\rtest_category:\x0btest_handleJ\x0ctest_created'


m2 = m1.ParseFromString(serialized)
print(m2)
data = apply(m1, m2)
print(data)







