import os
from selene import browser, be, have


def test_send_practice_form_(browser_config):
    # Открытие страницы Practice Form
    browser.open('/automation-practice-form')
    # Проверка страницы Practice Form
    browser.element('//h5[contains(text(), "Student Registration Form")]').should(have.text('Student Registration Form'))
    #Заполнение полей формы
    browser.element('#firstName').should(be.blank).type('Egor')
    browser.element('#lastName').should(be.blank).type('Letov')
    browser.element('#userEmail').should(be.blank).type('Letov_Perestroyka@home.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('8123456789')
    # Ввод даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-container').should(be.visible)
    browser.element('.react-datepicker__month-select').click()
    browser.element('//option[contains(text(), "September")]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('//option[contains(text(), "1964")]').click()
    browser.element('//div[contains(text(), "10")]').click()
    # Заполнение полей формы
    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').should(be.blank).type('Song and music')
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('ava.png'))
    # Личные данные
    browser.element('#currentAddress').should(be.blank).type('Brighton Beach  New York City')
    browser.element('#react-select-3-input').set_value('NCR').press_tab()
    browser.element('#react-select-4-input').set_value('Delhi').press_tab()
     # Отправка формы
    browser.element('#submit').click()
    # Окно и уведомление об успешной отправке
    browser.element('.modal-content').should(be.visible)
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    # Сверка полей формы с переданным ранее текстом
    browser.element('.table').all('tr').should(have.exact_texts(
        'Label Values',
        'Student Name Egor Letov',
        'Student Email Letov_Perestroyka@home.ru',
        'Gender Male',
        'Mobile 8123456789',
        'Date of Birth 10 September,1964',
        'Subjects',
        'Hobbies Music',
        'Picture ava.png',
        'Address Brighton Beach New York City',
        'State and City NCR Delhi'
                         )
    )
    # Закрытие окна уведомления
    browser.element('#closeLargeModal').click()