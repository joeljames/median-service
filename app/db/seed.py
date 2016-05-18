from app.median.repositories import ValueRepository


__all__ = [
    'Seed'
]


class Seed:
    """
    Seeds the database with data.
    Empties the entire collection first
    followed by creating new data
    """
    data = [3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]

    def __init__(self, data=None):
        self.repository = ValueRepository()
        self.seed_data = data or self.data
        self

    def clear_db(self):
        self.repository.delete_all()

    def seed_db(self):
        for value in self.seed_data:
            self.repository.create(value=value)

    def run(self):
        self.clear_db()
        self.seed_db()
