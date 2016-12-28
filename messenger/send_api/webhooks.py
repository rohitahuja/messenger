from datetime import datetime

from messages import (
    Sender,
    Recipient,
)


class WebhookMessaging(object):
    def __init__(self, sender, recipient, timestamp=None, **kwargs):
        self.sender = Sender(id=sender['id'])
        self.recipient = Recipient(id=recipient['id'])
        if timestamp is not None:
            # TODO: Validate time
            self.timestamp = datetime.utcfromtimestamp(timestamp / 1000)

        for key, value in kwargs.items():
            self.__dict__[key] = value

    @property
    def is_message(self):
        return hasattr(self, 'message')

    @property
    def is_received(self):
        return self.is_message and 'is_echo' not in self.message

    @property
    def is_echo(self):
        return self.is_message and 'is_echo' in self.message

    @property
    def has_quick_reply(self):
        return self.is_message and 'quick_reply' in self.message

    @property
    def has_text(self):
        return self.is_message and 'text' in self.message

    @property
    def has_attachments(self):
        return self.is_message and 'attachments' in self.message

    @property
    def is_delivery(self):
        return hasattr(self, 'delivery')

    @property
    def is_read(self):
        return hasattr(self, 'read')

    @property
    def is_postback(self):
        return hasattr(self, 'postback')


class WebhookEntry(object):
    def __init__(self, id, time, messaging):
        self.id = id
        # TODO: Validate time
        self.time = datetime.utcfromtimestamp(time / 1000)
        self.messaging = [
            WebhookMessaging(**m) for m in messaging
        ]


class Webhook(object):
    def __init__(self, payload):
        self.payload = payload

    @property
    def entries(self):
        return [
            WebhookEntry(**e) for e in self.payload['entry']
        ]
