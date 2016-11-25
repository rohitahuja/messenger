# Messenger Platform

This is a wrapper library for communicating with the Facebook Messenger Platform API. This is a reflection of https://github.com/geeknam/messengerbot, with some exceptions.

## Setup

If installing for the first time:
```
pip install -e git+git://github.com/rohitahuja/messenger_platform.git#egg=messenger_platform 
```

If updating within a project:
```
pip install update -e git+git://github.com/rohitahuja/messenger_platform.git#egg=messenger_platform 
```

## Includes
 - Sending messages to a user from a bot
 - Raising messenger related exceptions
 - Getting user profile information
 - Webhook response wrapping

## Does not include
 - Subscribing an app to get updates for a page (what does it do?)
 - Global access client initialized in __init__.py
 - Attachments object
 - Elements (button) object
 - Templates objects
 - Other messenger enhancements