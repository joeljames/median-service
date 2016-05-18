from invoke import task


from app.db.seed import Seed


__all__ = [
    'seed_db',
]


@task
def seed_db():
    """
    Task to seed the database.
    """
    Seed().run()
