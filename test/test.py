import os

import pytest
from selene import have, be, browser


def test_fill_form(open_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstname"]').type('Alexandra')
    browser.element('[id="lastname"]').type('Borland')
    browser.element('[id="userEmail"]').type('borland3711@gmail.com')
    browser.element('[id="gender-radio-2]').should(have.exact_text('Female')).click()
    browser.element('[id="userNumber"]').type('79992131514')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('react-datepicker__month-select').click()
    browser.element('[value="5"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1998"]').click()
    browser.element('[class="react-datepicker__month"]').click()
    browser.element('[value="18"]').click()
    browser.element('[id="subjectsInput"]').type('m')
    # дальше не очень понимаю каким действием выбрать что-то из выпадающего списка.
    # нахожу кусок кода для списка, но при нажатии на стрелку моя буква стирается и список исчезает
    browser.element('[class="col-md-9 col-sm-12"]').should(have.exact_text('Music')).click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('picture\img.png'))
    browser.element('[id="currentAddress"]').type('Moscow')
    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-input"]').click()
    browser.element('[id="city"]').click()
    browser.element('[id = "react-select-4-input""]').click()
    browser.element('[id="submit"]').click()
    #checking the form
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    browser.element('[class="modal-body"]').should(have.text('Alexandra'))
    browser.element('[class="modal-body"]').should(have.text('Borland'))
    browser.element('[class="modal-body"]').should(have.text('borland3711@gmail.com'))
    browser.element('[class="modal-body"]').should(have.text('Female'))
    browser.element('[class="modal-body"]').should(have.text('79992131514'))
    browser.element('[class="modal-body"]').should(have.text('18 June,1998'))
    browser.element('[class="modal-body"]').should(have.text('Math'))
    browser.element('[class="modal-body"]').should(have.text('Music'))
    browser.element('[class="modal-body"]').should(have.text('img.png'))
    browser.element('[class="modal-body"]').should(have.text('Moscow'))
    browser.element('[class="modal-body"]').should(have.text('NCR Delhi'))