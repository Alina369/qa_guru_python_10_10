from selene import browser, be, have, by

from demoqa_tests import resources


class RegistrationPage:

    def open(self):
        browser.open("/")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def email(self, value):
        browser.element("#userEmail").type(value)

    def genger(self, value):
        female = (browser.element(f'[name=gender][value={value}]+label'))
        female.click()

    def number(self, value):
        browser.element("#userNumber").type(value)

    def date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(f".react-datepicker__day--0{day}").click()

    def fill_subjects(self, value):
        browser.element("#subjectsInput").should(be.blank).type(value).press_enter()

    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture.form-control-file').send_keys(resources.path(value))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element("#state").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()

    def select_city(self, value):
        browser.element("#city").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()

    def submit(self):
        browser.element("#submit").click()

    def should_registered_user_with(self, full_name, email, gender, number, date_of_birth, subjects, hobby, picture, address,
                                    state_and_city):
        browser.element('.table').all('td').even.should(have.texts(
            full_name,
            email,
            gender,
            number,
            date_of_birth,
            subjects,
            hobby,
            picture,
            address,
            state_and_city))
