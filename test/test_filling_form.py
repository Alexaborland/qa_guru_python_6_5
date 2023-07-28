import os

import pytest
from selene import have, be, browser


def test_student_registration_form(browser_open):
    browser.open('/automation-practice-form')

    # First and Second Name
    browser.element('[id=firstName]').type('Alexandra')
    browser.element('[id="lastName"]').type('Borland')
    # E-mail
    browser.element('[id="userEmail"]').type('borland3711@gmail.com')
    # Sex
    browser.element('[name=gender][value=Female]+label').click()
    # Number
    browser.element('[id=userNumber]').type('9992131512')
    # Date of birth
    browser.element('[id=dateOfBirthInput]').click()
    browser.element('.react-datepicker__month-select').send_keys('June')
    browser.element('.react-datepicker__year-select').click().send_keys('1998')
    browser.element(f'.react-datepicker__day--0{15}').click()
    # Hobbies
    browser.element('[id="subjectsInput"]').type('Maths').press_enter()
    browser.all('.custom-control').element_by(have.exact_text('Music')).click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('picture\img.png'))
    # Address
    browser.element('[id="currentAddress"]').type('Kondratyevsky prospect')
    browser.element('[id="state"]').click()
    browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('[id="city"]').click()
    browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text('Karnal')).click()
    # Submit
    browser.element('[id="submit"]').click()

    # Checking
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    browser.element('[class="modal-body"]').should(have.text('Alexandra'))
    browser.element('[class="modal-body"]').should(have.text('Borland'))
    browser.element('[class="modal-body"]').should(have.text('borland3711@gmail.com'))
    browser.element('[class="modal-body"]').should(have.text('Female'))
    browser.element('[class="modal-body"]').should(have.text('9992131512'))
    browser.element('[class="modal-body"]').should(have.text('18 June,1998'))
    browser.element('[class="modal-body"]').should(have.text('Math'))
    browser.element('[class="modal-body"]').should(have.text('Music'))
    browser.element('[class="modal-body"]').should(have.text('img.png'))
    browser.element('[class="modal-body"]').should(have.text('Kondratyevsky prospect'))
    browser.element('[class="modal-body"]').should(have.text('Haryana Karnal'))
