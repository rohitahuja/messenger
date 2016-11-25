import os
from django.test import TestCase
from messenger_platform import MessengerClient
from messenger_platform.send_api import MessagesRequest
from messenger_platform.send_api.messages import Message, Sender
from messenger_platform.send_api.quick_replies import QuickReply, QuickReplies
from messenger_platform.thread_settings import ThreadSettingsRequest
from messenger_platform.thread_settings.thread_objects import CallToActions, MenuItem, Greeting, Payload

token = os.environ.get('PAGE_ACCESS_TOKEN')


class MessengerTestCase(TestCase):
    def setUp(self):
        self.client = MessengerClient(token)
        self.senders = [Sender(id='1174792065929365')]#, Sender(id='1021443131312051')]

    def test_quick_replies(self):
        quick_replies = QuickReplies()
        for i in range(5):
            option = 'option%s' % i
            qr = QuickReply('text', option, option)
            quick_replies.add_quick_reply(qr)
        message = Message(text='ay catch these options', quick_replies=quick_replies)
        for sender in self.senders:
            request = MessagesRequest(sender, message)
            self.client.send(request)

    def test_persistent_menu(self):
        call_to_actions = CallToActions()
        for i in range(5):
            title = 'bot boy %s' % i
            payload = 'menu payload %s' % i
            menu_item = MenuItem.create_postback(title=title, payload=payload)
            call_to_actions.add_menu_item(menu_item)
        request = ThreadSettingsRequest.create_persistent_menu(call_to_actions)
        self.client.send(request)

    def test_get_started(self):
        call_to_actions = CallToActions()
        payload = Payload('user defined payload for get started')
        call_to_actions.add_payload(payload)
        request = ThreadSettingsRequest.create_get_started_button(call_to_actions)
        self.client.send(request)

    def test_greeting(self):
        greeting = Greeting(text='ay {{user_first_name}} hop in')
        request = ThreadSettingsRequest.create_greeting(greeting)
        self.client.send(request)
