from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    movie = get_movie("Lagaan", 1997)
    movie =None
    if movie:
        print("Get movie succeeded:")
        pprint(movie)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    table.put_item( Item = {'title': 'Lagaan','year': 1997,'info': {'looks': {'actors': {'Hero': 'Amir Khan', 'Heroin': 'Preeti Zinta'}}},})