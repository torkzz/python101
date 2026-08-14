from person import Person


class Student(Person):

    def __init__(self):
        super().__init__()

        self._course = ""
        self._year_level = 0

    @property
    def course(self) -> str:
        return self._course

    @course.setter
    def course(self, course: str):
        self._course = course

    @property
    def year_level(self) -> int:
        return self._year_level

    @year_level.setter
    def year_level(self, year_level: int):
        self._year_level = year_level
