from selene import have, command, browser

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).perform(command.js.scroll_into_view).click()
        browser.element('#userNumber').type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.date_of_birth_month)
        browser.element('.react-datepicker__year-select').type(user.date_of_birth_year)
        browser.element(f'.react-datepicker__day--0{user.date_of_birth_day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.text(user.hobby)).click()
        browser.element('#uploadPicture').set_value(resource.path(user.file))
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.city)
        ).click()
        browser.element('#submit').press_enter()
        return self

    def should_register_user_with(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
            user.subject,
            user.hobby,
            user.file,
            user.address,
            f'{user.state} {user.city}'))
        return self
