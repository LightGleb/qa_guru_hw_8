
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_fill_and_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_first_name('Глеб')
    registration_page.fill_last_name('Иванов')
    registration_page.fill_email('pipo@mail.ru')
    registration_page.select_gender('Male')
    registration_page.fill_phone_number('6666666666')
    registration_page.fill_date_of_birth('1980', 'June', '25')
    registration_page.fill_subject('Computer Science')
    registration_page.select_hobby('Music')
    registration_page.upload_picture('foto.jpg')
    registration_page.fill_address('Leningradskaya Street 23')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')

    registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        'Глеб Иванов',
        'pipo@mail.ru',
        'Male',
        '6666666666',
        '25 June,1980',
        'Computer Science',
        'Music',
        'foto.jpg',
        'Leningradskaya Street 23',
        'Haryana Karnal'
    )
