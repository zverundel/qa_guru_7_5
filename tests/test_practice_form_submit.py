import os
from selene import browser, be, have, command


def test_practice_form(browser_open_url):
    # Заполнение основной информации
    browser.open('/automation-practice-form')
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

    #Выбор предмета
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()

    #Выбор хобби
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    #Загрузка картинки
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test_picture.jpg'))

    #Адрес
    browser.element('#currentAddress').should(be.blank).type('orehovo-zuevo, parcov, 15')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    #Проверка
    browser.all('.table>tbody>tr')[0].should(have.exact_text('Student Name Daniil Zverev'))
    browser.all('.table>tbody>tr')[1].should(have.exact_text('Student Email test@gmail.ru'))
    browser.all('.table>tbody>tr')[2].should(have.exact_text('Gender Male'))
    browser.all('.table>tbody>tr')[3].should(have.exact_text('Mobile 8977345674'))
    browser.all('.table>tbody>tr')[4].should(have.exact_text('Date of Birth 04 May,1998'))
    browser.all('.table>tbody>tr')[5].should(have.exact_text('Subjects Maths'))
    browser.all('.table>tbody>tr')[6].should(have.exact_text('Hobbies Sports, Reading, Music'))
    browser.all('.table>tbody>tr')[7].should(have.exact_text('Picture test_picture.jpg'))
    browser.all('.table>tbody>tr')[8].should(have.exact_text('Address orehovo-zuevo, parcov, 15'))
    browser.all('.table>tbody>tr')[9].should(have.exact_text('State and City NCR Noida'))