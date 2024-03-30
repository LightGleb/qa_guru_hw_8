import os

from selene import browser, have, command

import tests


def test_fill_and_submit_form():
    browser.open('/automation-practice-form')
    # WHEN
    browser.element('#firstName').type('Глеб')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('pipo@mail.ru')
    browser.all('.custom-radio').element_by(have.text('Male')).perform(command.js.scroll_into_view).click()
    browser.element('#userNumber').type('6666666666')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('June')
    browser.element('.react-datepicker__year-select').type('1980')
    browser.element(f'.react-datepicker__day--0{25}').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.all('.custom-checkbox').element_by(have.text('Music')).click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto.jpg')
        )
    )
    browser.element('#currentAddress').type('Leningradskaya Street 23')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Haryana')
    ).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Karnal')
    ).click()

    browser.element('#submit').press_enter()
    # THEN
    browser.element('.table').all('td').should(
        have.texts(
            ('Student Name', 'Глеб Иванов'),
            ('Student Email', 'pipo@mail.ru'),
            ('Gender', 'Male'),
            ('Mobile', '6666666666'),
            ('Date of Birth', '25 June,1980'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Music'),
            ('Picture', 'foto.jpg'),
            ('Address', 'Leningradskaya Street 23'),
            ('State and City', 'Haryana Karnal'),
        )
    )
