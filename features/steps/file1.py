from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@given(u'launched browser')
def step_impl(context):
    # print('File implemented')
    # raise NotImplementedError(u'STEP: When launched browser')
    # Creating Instance
    option = Options()

    # Working with the 'add_argument' Method to modify Driver Default Notification
    option.add_argument('--disable-notifications')

    # Passing Driver path alongside with Driver modified Options
    browser = webdriver.Chrome(executable_path= "E:\drivers\chromedriver_win32\chromedriver2_42.exe", chrome_options= option)

    # Do your stuff and quit your driver/ browser
    browser.get('https://visual-vocabulary.qa-9.money-media.com/compose/0?site=AG&chartType=bubble')
    browser.quit()


@when(u'launched browser')
def step_impl(context):
    print('File implemented')
    # raise NotImplementedError(u'STEP: When launched browser')


@then(u'Browser launched')
def step_impl(context):
    print('File implemented')
    # raise NotImplementedError(u'STEP: Then Browser launched')
