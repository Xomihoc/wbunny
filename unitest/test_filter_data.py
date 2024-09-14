from backend.filter.filter import FilterData
import unittest
from backend.exception import exception


filter_data = FilterData()


# Юнит-тесты
class TestPhoneValidation(unittest.TestCase):
    def setUp(self):
        self.valid_phone_numbers = [
            "123-456-7890",
            "(123)456-7890",
            "123.456.7890",
            "1234567890",
            "+7 123 456 7890",
            "123-4567-890",
            "7 123 456 7890",
            "+7(123)456-78-90",
            "7 (123) 456 78 90",
            "12345 67890",
            "+(123) 456-7890",
        ]

        self.invalid_phone_numbers = [
            "+1-234-567-8901",
            "+7 123 456 78",
            "+1 (234) 567-8901",
            "123-45-678",
            "+44 20 1234 5678",
            "(123) 456 789",
            "123-4567-89012",
            "234567890",
            "123456abcd", 
            "+7 (123) 456-78901",
        ]

    def test_valid_phone_numbers(self):
        for phone in self.valid_phone_numbers:
            self.assertTrue(filter_data.number_phone(number_phone=phone))

    def test_invalid_phone_numbers(self):
        for phone in self.invalid_phone_numbers:
            with self.assertRaises(exception.ScenariesWebApiFilterError.NumberPhoneError):
                filter_data.number_phone(number_phone=phone)


class TestUserNameTg(unittest.TestCase):

    def setUp(self):
        self.positive_examples = [
            "test@example",
            "user123@abc_def",
            "admin@data-2023",
            "name@value_with_hyphen",
            "@only_after",  # будет извлечено 'only_after'
            "validInput",
            "user-name",
            "data_123",
            "test123"
            "bad.string@data"  # Недопустимый символ .
        ]

        self.negative_examples = [
            "onlyAt@",         # Символ @ без текста после
            "noData@!",        # Неправильный символ после @
            "invalid@#%^",     # Недопустимые символы после @
            "test@data!",      # Недопустимый символ !
            "name@_value$",    # Недопустимый символ $
            "invalid@text*",   # Недопустимый символ *
            "user@exam ple",   # Пробел в строке
            "invalid#input",   # Недопустимый символ #
            "123@invalid!",    # Неправильный символ после @
        ]

    def test_valid_user_name_tg(self):
        for name in self.positive_examples:
            self.assertTrue(filter_data.user_name_tg(user_name_tg=name))

    def test_invalid_user_name_tg(self):
        for name in self.negative_examples:
            with self.assertRaises(exception.ScenariesWebApiFilterError.UserNameTgError):
                filter_data.user_name_tg(user_name_tg=name)


class TestVk(unittest.TestCase):

    def setUp(self):
        self.positive_examples = [
            "test@example",
            "user123@abc_def",
            "admin@data-2023",
            "name@value_with_hyphen",
            "@only_after",  # будет извлечено 'only_after'
            "validInput",
            "user-name",
            "data_123",
            "test123"
            "bad.string@data"  # Недопустимый символ .
        ]

        self.negative_examples = [
            "onlyAt@",         # Символ @ без текста после
            "noData@!",        # Неправильный символ после @
            "invalid@#%^",     # Недопустимые символы после @
            "test@data!",      # Недопустимый символ !
            "name@_value$",    # Недопустимый символ $
            "invalid@text*",   # Недопустимый символ *
            "user@exam ple",   # Пробел в строке
            "invalid#input",   # Недопустимый символ #
            "123@invalid!",    # Неправильный символ после @
        ]

    def test_valid_vk(self):
        for name in self.positive_examples:
            self.assertTrue(filter_data.vk(vk=name))

    def test_invalid_vk(self):
        for name in self.negative_examples:
            with self.assertRaises(exception.ScenariesWebApiFilterError.VkError):
                filter_data.vk(vk=name)

                

class TestVk(unittest.TestCase):

    def setUp(self):
        self.positive_examples = [
            "test@example",
            "user123@abc_def",
            "admin@data-2023",
            "name@value_with_hyphen",
            "@only_after",  # будет извлечено 'only_after'
            "validInput",
            "user-name",
            "data_123",
            "test123"
            "bad.string@data"  # Недопустимый символ .
        ]

        self.negative_examples = [
            "onlyAt@",         # Символ @ без текста после
            "noData@!",        # Неправильный символ после @
            "invalid@#%^",     # Недопустимые символы после @
            "test@data!",      # Недопустимый символ !
            "name@_value$",    # Недопустимый символ $
            "invalid@text*",   # Недопустимый символ *
            "user@exam ple",   # Пробел в строке
            "invalid#input",   # Недопустимый символ #
            "123@invalid!",    # Неправильный символ после @
        ]

    def test_valid_vk(self):
        for name in self.positive_examples:
            self.assertTrue(filter_data.vk(vk=name))

    def test_invalid_vk(self):
        for name in self.negative_examples:
            with self.assertRaises(exception.ScenariesWebApiFilterError.VkError):
                filter_data.vk(vk=name)


class TestMail(unittest.TestCase):

    def setUp(self):
        self.positive_examples = [
            "test@example.com",
            "user.name@sub.domain.com",
            "simple123@mail.ru",
            "long.name.with.dots@domain.info",
            "verylongusername@verylongdomain.com",
            "valid_email@example.org",
            "test123@domain.com",
            "info@mywebsite.info",
            "test.email+alex@leetcode.com"
        ]

        self.negative_examples = [
            "a@b.co",
            "a@b.c",                     # Логин слишком короткий
            "@missingusername.com",      # Отсутствует логин
            "missingat.com",             # Отсутствует символ @
            "username@.com",             # Отсутствует доменная часть перед точкой
            "username@domain..com",      # Две точки подряд в домене
            "username@domain.z",         # Доменная зона слишком короткая
            "username@domain.com.",       # Точка в конце
            "invalid_email@domain.c",    # Логин слишком длинный
            "username@domain..info",     # Две точки подряд
            "us@ername@domain.com"       # Слишком много символов @
        ]

    def test_valid_mail(self):
        for name in self.positive_examples:
            self.assertTrue(filter_data.mail(mail=name))

    def test_invalid_mail(self):
        for name in self.negative_examples:
            with self.assertRaises(exception.ScenariesWebApiFilterError.MailError):
                filter_data.mail(mail=name)


if __name__ == '__main__':  

    unittest.main()
