from selene import have

from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    #WHEN
    registration_page.fill_first_name("Anna")
    registration_page.fill_last_name("Ivanova")
    registration_page.email("testemail@mail.ru")

    registration_page.genger('Female')
    registration_page.number("8952333222")
    registration_page.date_of_birth('1994', 'March', '24')

    registration_page.fill_subjects("a")
    registration_page.select_hobbies('Sports')
    registration_page.upload_picture('orig.jpg')
    
    registration_page.fill_address('Lenina Street 18')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')

    registration_page.submit()


    # THEN
    registration_page.should_registered_user_with(
            'Anna Ivanova',
            'testemail@mail.ru',
            'Female',
            '8952333222',
            '24 March,1994',
            'Maths',
            'Sports',
            'orig.jpg',
            'Lenina Street 18',
            'NCR Delhi'
    )






