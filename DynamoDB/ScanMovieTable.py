import boto3
import pprint
from boto3.dynamodb.conditions import Attr, Key


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')

response = table.scan(
    FilterExpression=Key('year').lte(2013)
)
items = response['Items']
pprint.pprint(items)