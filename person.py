from faker import Faker


class Person:

    def __init__(self):
        self._name = ""
        self._age = 0
        self.f = Faker()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def _generate_random_first_name(self) -> str:
        return self.f.first_name()

    def __generate_random_first_name(self) -> str:
        return self.f.first_name()

    def retrieve_random_name(self) -> str:
        return self.__generate_random_first_name()

    @staticmethod
    def _generate_random_first_name_kana() -> str:
        f = Faker("ja-JP")
        return f.first_kana_name()
