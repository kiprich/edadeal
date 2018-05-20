from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string

class Bot:

    def tel_recon(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'c:\Users\5trike\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe') # or Firefox() or smth else
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')


    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        image.crop((x, y, x+width, y+height)).save('tel.gif')
        self.tel_recon()

    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/telefony/telefon_lenovo_a6010_1469485747?slocation=637640')
        button = self.driver.find_element_by_xpath(
            '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]//*')
        button.click()

        sleep(3)

        self.take_screenshot()

        image = self.driver.find_element_by_xpath(
            '//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location
        size = image.size
        print(size)

        self.crop(location, size)


def main():
    b = Bot()


if __name__ == '__main__':
    main()