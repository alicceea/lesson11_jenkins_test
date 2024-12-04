import allure
from allure_commons.types import AttachmentType
from selene import browser


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

def add_logs():
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

def add_html():
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')