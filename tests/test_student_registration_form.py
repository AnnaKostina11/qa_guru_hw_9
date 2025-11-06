from pages.registration_page import RegistrationPage



def test_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Anna')
    registration_page.fill_last_name('Kostina')
    registration_page.fill_email('111name@example.com')
    registration_page.select_gender('Female')
    registration_page.mobile_number('8788888888')
    registration_page.select_date_of_birth('18 June 2025')
    registration_page.fill_subjects("Computer Science")
    registration_page.fill_hobbies('Reading')
    registration_page.upload_picture('resources/duck.jpg')
    registration_page.fill_address('Moscow')
    registration_page.select_state('Uttar Pradesh')
    registration_page.select_city('Agra')
    registration_page.click_submit()

    # THEN
    registration_page.should_registered_user_with('Anna Kostina',
                                           '111name@example.com',
                                           'Female',
                                           '8788888888',
                                           '18 June,2025',
                                           'Computer Science',
                                           'Reading',
                                           'duck.jpg',
                                           'Moscow',
                                           'Uttar Pradesh Agra'
                                           )