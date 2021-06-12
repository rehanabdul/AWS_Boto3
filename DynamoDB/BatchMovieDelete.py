import boto3
import pprint
from boto3.dynamodb.conditions import Attr, Key


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')

batch  = table.batch_writer()
with table.batch_writer() as batch:
    batch.delete_item(
        Key={
            'year': 2003,
            'title': 'Grind'
        }
    )
    batch.delete_item(
        Key={
            'year': 2003,
            'title': 'Gothika'
        }
    )
    