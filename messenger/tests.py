# import os
# from django.test import TestCase

# from messenger import (
#     MessengerClient,
#     send_api,
#     thread_settings,
# )
# from send_api import (
#     MessagesRequest,
#     messages,
#     quick_replies,
# )
# from thread_settings import (
#     ThreadSettingsRequest,
#     thread_objects,
# )

# token = os.environ.get('PAGE_ACCESS_TOKEN')


# class MessengerTestCase(TestCase):
#     def setUp(self):
#         self.client = MessengerClient(token)
#         self.senders = [messages.Sender(id='1174792065929365')]#, Sender(id='1021443131312051')]

#     def test_quick_replies(self):
#         qrs = quick_replies.QuickReplies()
#         for i in range(5):
#             option = 'option%s' % i
#             qr = QuickReply('text', option, option)
#             qrs.add_quick_reply(qr)
#         message = messages.Message(text='ay catch these options', quick_replies=quick_replies)
#         for sender in self.senders:
#             request = MessagesRequest(sender, message)
#             self.client.send(request)

#     def test_persistent_menu(self):
#         call_to_actions = CallToActions()
#         for i in range(5):
#             title = 'bot boy %s' % i
#             payload = 'menu payload %s' % i
#             menu_item = MenuItem.create_postback(title=title, payload=payload)
#             call_to_actions.add_menu_item(menu_item)
#         request = ThreadSettingsRequest.create_persistent_menu(call_to_actions)
#         self.client.send(request)

#     def test_get_started(self):
#         call_to_actions = CallToActions()
#         payload = Payload('user defined payload for get started')
#         call_to_actions.add_payload(payload)
#         request = ThreadSettingsRequest.create_get_started_button(call_to_actions)
#         self.client.send(request)

#     def test_greeting(self):
#         greeting = Greeting(text='ay {{user_first_name}} hop in')
#         request = ThreadSettingsRequest.create_greeting(greeting)
#         self.client.send(request)
