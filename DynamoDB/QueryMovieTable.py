import boto3
import pprint
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')

response = table.query(
    KeyConditionExpression=Key('year').eq(2013)
)
items = response['Items']
pprint.pprint(items)


