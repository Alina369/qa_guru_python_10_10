from selene import browser, be, have, by

from demoqa_tests.resources import path


def test_student_registration_form():
    browser.open("/")

    #WHEN
    browser.element("#firstName").type("Anna")
    browser.element("#lastName").type("Ivanova")
    browser.element("#userEmail").type("testemail@mail.ru")

    female = (browser.element('[name=gender][value=Female]+label'))
    female.click()

    browser.element("#userNumber").type("8952333222")

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element('option[value="2"]').click()

    browser.element(".react-datepicker__year-select").element('option[value="1994"]').click()
    browser.element(".react-datepicker__day--024").click()
    browser.element("#subjectsInput").should(be.blank).type("a").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture.form-control-file').send_keys(path('orig.jpg'))
    # browser.element('#uploadPicture.form-control-file').send_keys(os.path.abspath('../resources/orig.jpg'))

    browser.element('#currentAddress').type('address')
    browser.element("#state").should(be.clickable).click()
    browser.element(by.text('NCR')).should(be.clickable).click()
    browser.element("#city").should(be.clickable).click()
    browser.element(by.text('Delhi')).should(be.clickable).click()

    browser.element("#submit").click()

    # THEN
    browser.element('.table').all('td').even.should(have.texts(
        'Anna Ivanova',
        'testemail@mail.ru',
        'Female',
        '8952333222',
        '24 March,1994',
        'Maths',
        'Sports',
        'orig.jpg',
        'address',
        'NCR Delhi'))




