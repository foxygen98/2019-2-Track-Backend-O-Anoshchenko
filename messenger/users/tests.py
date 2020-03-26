import json
from django.urls import reverse
from django.test import TestCase, Client
from users.models import User
from selenium import webdriver

class TestUsers(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="TestUser", nick="TestNick")

    def test_profile(self):
        response = self.client.get(reverse('profile', kwargs={'prof_id': self.user.id}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['profile']['nick'], 'TestNick')

    def test_contacts(self):
        response = self.client.get(reverse('contacts'))
        self.assertTrue(response.status_code == 200)
        self.assertJSONEqual(response.content, '{"contacts": "test"}')

    def test_search_profile(self):
        response = self.client.get(reverse('search_profile', kwargs={'nick': self.user.nick}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['users'], [{"nick": "TestNick"}])

class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_return_back(self):
        driver = self.driver
        driver.get('https://foxygen98.github.io/2019-2-Track-Frontend-O-Anoshchenko/#/profile')
        # находим кнопку для возврата и кликаем
        elem = driver.find_element_by_class_name('Header_ReturnButton__1F3mW')
        elem.click()
        # проверяем, что мы перешли к списку чатов, т.е. имеем верное название в Header
        driver.find_element_by_class_name('Header_Name__3m-mq')

    def tearDown(self):
        self.driver.close()
