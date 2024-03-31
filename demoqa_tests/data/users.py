from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str


student = User(first_name='Глеб',
               last_name='Иванов',
               email='pipo@mail.ru',
               gender='Male',
               phone_number='6666666666',
               date_of_birth_year='1980',
               date_of_birth_month='June',
               date_of_birth_day='25',
               subject='Computer Science',
               hobby='Music',
               file='foto.jpg',
               address='Leningradskaya Street 23',
               state='Haryana',
               city='Karnal')
