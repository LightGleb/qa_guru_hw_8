from selene import have, command, browser

from demoqa_tests import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, value):
        browser.all('.custom-radio').element_by(have.text(value)).perform(command.js.scroll_into_view).click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def select_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.text(value)).click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').set_value(resource.path(value))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, name):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def should_registered_user_with(self,
                                    fullname, email, gender, phone_number, birthday,
                                    subject, hobby, photo, address, state_city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            fullname,
            email,
            gender,
            phone_number,
            birthday,
            subject,
            hobby,
            photo,
            address,
            state_city
        ))
        return self
