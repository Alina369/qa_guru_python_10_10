from demoqa_tests.data.users import student
from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.fill(student)
    registration_page.submit_the_form()

    # THEN
    registration_page.should_registered_user_with(student)



