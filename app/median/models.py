import mongoengine as me

from app.shared.utils import utc_now


__all__ = [
    'Value',
]


class Value(me.Document):
    value = me.IntField(required=True)
    created_at = me.DateTimeField(required=True, default=utc_now)

    meta = {
        'collection': 'value',
        'ordering': ['+value']
    }

    def __repr__(self):
        return '<Value(%r) - (%r)>' % (self.id, self.value)
