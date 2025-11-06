from data import users
from pages.registration_page import RegistrationPage


def test_student_registration_form(open_browser):
    registration_page = RegistrationPage()
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)