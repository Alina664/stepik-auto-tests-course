import pytest
import time
import math

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    link = f"{link}/"
    browser.get(link)
    time.sleep(3)
    input1 = browser.find_element_by_class_name("textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(2)
    ans = browser.find_element_by_css_selector("div.smart-hints__feedback.hints__component.hints__component_showed.ember-view")
    welcome_text = ans.text 
    assert "Correct!" == welcome_text
    
    
