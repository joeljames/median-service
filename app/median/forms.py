from flask_wtf import Form
from wtforms.fields.html5 import IntegerField
from wtforms import validators


__all__ = [
    'ValuePostForm',
]


class ValuePostForm(Form):

    """
    The value post form.
    Also, takes care of the validations on the value field.
    """

    value = IntegerField(
        'value',
        [
            validators.Required(message='Must provide a valid integer value.'),
        ]
    )

    def save(self, repository):
        data = {
            'value': self.data.get('value')
        }
        return repository.create(**data)
