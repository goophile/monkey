from mongoengine import connect, errors
from .model import User, TextPost


def connect_monkey():
    # host is the same as in docker-compose.yaml
    connect('monkey', host='mongo')


def insert_data_for_query():
    """
    Insert data for query demonstration.
    """
    try:
        _insert_hamlet()
    except errors.NotUniqueError:
        pass


def _insert_hamlet():
    william = User(
        email='william@monkey.com',
        first_name='William',
        last_name='Shakespeare',
    ).save()

    TextPost(
        title='Hamlet',
        author=william,
        content=('Finally came out with this sentense after hitting keys at random '
                 'on a typewriter keyboard for an infinite amount of time.'),
        tags=['infinite', 'monkey'],
    ).save()
