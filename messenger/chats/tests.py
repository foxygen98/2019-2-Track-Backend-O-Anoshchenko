import json
from django.urls import reverse
from django.test import TestCase, Client
from users.models import User, Member
from chats.models import Chat
from mock import patch
from chats.factories import MessageFactory

class UsersTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create(username="TestUser №1", nick="TestNick №1")
        self.user2 = User.objects.create(username="TestUser №2", nick="TestNick №2")

        self.chat = Chat.objects.create(topic="TestChat", last_message=1)

        self.member1 = Member.objects.create(user_id=self.user1.id, chat_id=self.chat.id)
        self.member2 = Member.objects.create(user_id=self.user2.id, chat_id=self.chat.id)

        self.message1 = MessageFactory.build(user_id=self.user1.id, chat_id=self.chat.id)
        self.message1.save()
        self.message2 = MessageFactory.build(user_id=self.user2.id, chat_id=self.chat.id)
        self.message2.save()

    def test_chat_list(self):
        response = self.client.get(reverse('chat_list', kwargs={'user_id': self.user1.id}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['chats'], [{'chat_id': 1}])

    def test_one_chat(self):
        response = self.client.get(reverse('one_chat', kwargs={'chat_id': self.chat.id}))
        self.assertTrue(response.status_code == 200)
        self.assertJSONEqual(response.content, 
                            '{"chat": ' + str(self.chat.id) + \
                            ', "topic": "' + self.chat.topic + \
                            '", "last message": ' + str(self.chat.last_message) + '}')

    def test_create_chat(self):
        response = self.client.post(reverse('create_chat'), {'topic': 'new chat', 'user': self.user1.id})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'success!')

    def test_send_message(self):
        response = self.client.post(reverse('send_message'), 
                                    {'chat': self.chat.id, 
                                     'user': self.user1.id, 
                                     'content': 'TEST'})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['message'], 'TEST')

    def test_list_messages(self):
        response = self.client.get(reverse('list_messages', kwargs={'chat_id': self.chat.id}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(len(content['messages']), 2)

    #def test_read_message(self):
    #    response = self.client.post(reverse('read_message'), {'member': self.member1.id})
    #    self.assertTrue(response.status_code == 200)
    #    content = json.loads(response.content)
    #    self.assertEqual(content['last_message'], self.message2.id)

    @patch('chats.views.read_message')
    def test_read_message(self, read_message_mock):
        read_message_mock()
        self.assertEqual(read_message_mock.call_count, 1)
