from messenger import BaseMessengerObject


class BaseTemplateObject(BaseMessengerObject):
    # put function like this in base class
    def add_element(self, elements, element):
        if len(elements) == self.ELEMENTS_LIMIT:
            raise ValueError('cannot have more than %s elements' % self.ELEMENTS_LIMIT)
        elements.append(element)


class ButtonTemplate(BaseTemplateObject):

    ELEMENTS_LIMIT = 3
    template_type = "button"  # validate existence of template_type

    def __init__(self, text):
        self.text = text
        self.buttons = []

    def add_button(self, button):
        self.add_element(self.buttons, button)

    def to_dict(self):
        return {
            'template_type': self.template_type,
            'text': self.text,
            'buttons': [
                button.to_dict() for button in self.buttons
            ]
        }
