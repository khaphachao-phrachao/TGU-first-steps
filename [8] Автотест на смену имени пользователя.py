# ---------------------------------------------------------------------------------------------------------------------
# Импортируем необходимые модули.
# ---------------------------------------------------------------------------------------------------------------------
from selene.support.shared import browser
from selene import be, have


# ---------------------------------------------------------------------------------------------------------------------
# Объявляем функцию.
# ---------------------------------------------------------------------------------------------------------------------
def test_image():
    browser.open('http://test.qahunter.ru/')
    browser.element('/html/body/header/div/nav/ul/li[4]/a').click()                          # переходим к форме входа
    browser.element('//*[@id="formInput#text"]').should(be.blank).type('some_user')          # вводим логин
    browser.element('//*[@id="formInput#passowrd"]').should(be.blank).type('some0password')  # вводим пароль
    browser.element('/html/body/div[1]/div/form/div[3]/input').click()                       # нажимаем войти

    browser.element('/html/body/main/div/div/div[1]/div/div/a').click()                      # настройки профиля
    browser.element('//*[@id="id_name"]').clear().type('new_user')                           # меняем имя
    browser.element('/html/body/main/div/div/form/input[2]').click()                         # сохраняем

    # -----------------------------------------------------------------------------------------------------------------
    # Проверяем, что смена имени прошла успешно.
    # -----------------------------------------------------------------------------------------------------------------
    browser.element('/html/body/main/div/div/div[1]/div/div/h2').should(have.text('new_user'))

    browser.element('/html/body/main/div/div/div[1]/div/div/a').click()
    browser.element('//*[@id="id_name"]').clear().type('some_user')                          # меняем имя на прежнее

    browser.element('/html/body/header/div/nav/ul/li[6]/a').click()                          # выходим из профиля
