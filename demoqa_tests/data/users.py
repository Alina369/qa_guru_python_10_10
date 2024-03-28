import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth: str
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
    date_of_birth="1999 May,24",
    subjects='a',
    hobbies='1',
    picture='orig.jpg',
    address='Moscowskaya Street 18',
    state='NCR',
    city='Delhi',
)
