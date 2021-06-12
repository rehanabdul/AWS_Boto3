import boto3
import pprint
from boto3.dynamodb.conditions import Attr, Key


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')

batch  = table.batch_writer()
with table.batch_writer() as batch:
    batch.put_item(
        Item={'info': {'actors': ['Cecile De France', 'Maiwenn', 'Philippe Nahon'],
           'directors': ['Alexandre Aja'],
           'genres': ['Horror', 'Mystery', 'Thriller'],
           'image_url': 'http://ia.media-imdb.com/images/M/MV5BNzEzMjEzMDI5N15BMl5BanBnXkFtZTcwNDc0ODkyMQ@@._V1_SX400_.jpg',
           'plot': 'Two college friends, Marie and Alexa, encounter loads of '
                   "trouble (and blood) while on vacation at Alexa's parents' "
                   'country home when a mysterious killer invades their quiet '
                   'getaway.',
           'rank': 3017,
           'rating': 6,
           'release_date': '2003-06-18T00:00:00Z',
           'running_time_secs': 5460},
    'title': 'Haute tension',
    'year': 2003}
    )
    batch.put_item(
        Item={'info': {'actors': ['Jennifer Connelly', 'Ben Kingsley', 'Ron Eldard'],
           'directors': ['Vadim Perelman'],
           'genres': ['Drama'],
           'image_url': 'http://ia.media-imdb.com/images/M/MV5BMTIzMjQ5NzM2M15BMl5BanBnXkFtZTYwMzU2NDY3._V1_SX400_.jpg',
           'plot': 'An abandoned wife is evicted from her house and starts a '
                   "tragic conflict with her home's new owners.",
           'rank': 3950,
           'rating': 7,
           'release_date': '2003-12-19T00:00:00Z',
           'running_time_secs': 7560},
  'title': 'House of Sand and Fog',
  'year':2003}
    )