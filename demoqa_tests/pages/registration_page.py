from selene import browser, have, be, by

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(
            f".react-datepicker__day--0{day}"
        ).click()

    def should_registered_user_with(self, fullname, email, gender, number, date_of_birth, subjects, hobbies, picture, address, city):
        browser.element('.table').all('td').even.should(have.texts(
            fullname,
            email,
            gender,
            number,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            address,
            city))

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def select_gender(self, value):
        female = (browser.element(f'[name=gender][value={value}]+label'))
        female.click()

    def fill_number(self, value):
        browser.element("#userNumber").type(value)

    def fill_subjects(self, value):
        browser.element("#subjectsInput").should(be.blank).type(value).press_enter()

    def select_hobbies(self, value):
        browser.element(f'[for="hobbies-checkbox-{value}"]').click()

    def upload_picture(self, value):
        browser.element('#uploadPicture.form-control-file').send_keys(resource.path(value))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element("#state").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()

    def select_city(self, value):
        browser.element("#city").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()

    def submit_the_form(self):
        browser.element("#submit").click()

    def fill(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_number(user.number)
        self.date_of_birth(user.date_of_birth)
        self.fill_subjects(user.subjects)
        self.select_hobbies(user.hobbies)
        self.upload_picture(user.picture)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
