# class Car:
#
#     def __init__(self):
#         self._modules = []
#
#     def __add__(self, other):
#         self._modules.append(other)
#         return self
#
# car = Car()
# module = 'Кондиционер'
#
# car + module + 'ГУР'
# print(car._modules)

# class Human:
#
#     @staticmethod
#     def say(what):
#         print('I am say', what)
#
# Human.say('hello')



class MyDict(dict):

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        print(key, value)

    def __getitem__(self, item):
        print(item)
        return super().__getitem__(item)

my_dict = MyDict()
my_dict['name'] = 'Ivan'
print(my_dict['name'])

# ljust, rjust
# sort( key=my_func)