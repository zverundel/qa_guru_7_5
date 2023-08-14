import os
from selene import browser, be, have, command


def test_practice_form():
    # Заполнение основной информации
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Daniil').press_tab()
    browser.element('#lastName').should(be.blank).type('Zverev').press_tab()
    browser.element('#userEmail').should(be.blank).type('test@gmail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('89773456745').press_tab()

    # Выбор даты рожедения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="4"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1998"]').perform(command.js.scroll_into_view).click()
    browser.element('[aria-label="Choose Monday, May 4th, 1998"]').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test_picture.jpg'))
    browser.element('#currentAddress').should(be.blank).type('orehovo-zuevo, parcov, 15')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Student Name Daniil Zverev'
                                               and 'Student Email test@gmail.ru'
                                               and 'Gender Male'
                                               and 'Mobile 8977345674'
                                               and 'Date of Birth 04 May,1998'
                                               and 'Subjects Maths'
                                               and 'Hobbies Sports, Reading, Music'
                                               and 'Picture test_picture.jpg'
                                               and 'Address orehovo-zuevo, parcov, 15'
                                               and 'State and City NCR Noida'))