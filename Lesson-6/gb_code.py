# class Phone:
#
#     def __init__(self, model, color='black'):
#         print('Создается объект типа телефон!')
#         self._model = model
#         self._color = color
#
#     # Getter
#     def get_model(self):
#         return self._model
#
#     # Setter
#     def set_color(self, new_color):
#         if new_color in ('black', 'red', 'white'):
#             self._color = new_color
#         else:
#             print('Вы выбрали некорректный цвет!')
#
#     def _show_boot_logo(self):
#         print('Loading..', self._model)
#
#     def call(self):
#         self._show_boot_logo()
#         print(self._model, 'calling')
#
#     def sms(self):
#         self._show_boot_logo()
#         print(self._model, 'sending sms...')
#
# phone = Phone('Samsung', 'red')
# phone.call()
# phone.sms()
# print(phone.get_model())


# class Phone:
#
#     def __init__(self, model):
#         self._model = model
#         self._id = 127631263812683912837
#
#     @property
#     def model(self):
#         return f'{self._model} {self._id}'
#
#
# phone = Phone('Нокия')
# print(phone.model)

class Phone:

    def __init__(self, model):
        self.model = model
        # Куча кода, который инициализует наш объект

    def call(self):
        print(self.model, 'calling...')

    def sms(self):
        print('sms...')


class Smartphone(Phone):

    def sms(self):
        print('sms with smiles!')

    def email(self):
        print('email...')

    def internet(self):
        print('internet...')

    def app(self):
        print('app...')


class Iphone(Smartphone):

    def player(self):
        print('music...')

    def browser(self):
        print('browser...')


class NextGenSmartphone(Iphone):

    def __init__(self, model, dna):
        super().__init__(model)
        # Phone().__init__(self, model)
        self.dna = dna

    def touch_id(self):
        print('touch id..')

    def face_id(self):
        print('face id...')


phone = NextGenSmartphone('Huawei Honor', '18723187236')
phone1 = Phone('Nokia')
phone2 = Iphone('Iphone 10')

def call_station(some_phone):
    some_phone.call()

call_station(phone)
call_station(phone1)
call_station(phone2)


##### ДЗ от меня!!!! #####

