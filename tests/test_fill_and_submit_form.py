from demoqa_tests.data import users
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_register_user_with(student)
