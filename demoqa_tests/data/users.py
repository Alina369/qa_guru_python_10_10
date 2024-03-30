import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    year: str
    month: str
    day: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str



student = User(
    first_name='Anna',
    last_name='Ivanova',
    email='testemail@mail.ru',
    gender='Female',
    number="8952333222",
    year='1999',
    month='May',
    day='24',
    subjects='Maths',
    hobbies='Sports',
    picture='orig.jpg',
    address='Moscowskaya Street 18',
    state='NCR',
    city='Delhi',
)
