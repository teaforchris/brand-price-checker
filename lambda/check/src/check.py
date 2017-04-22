from pprint import pprint
from lxml import html
import boto3
import requests
import re
import decimal
import json

xpath_map = {
    'sainsburys': '//p[@class="pricePerUnit"]/text()'
}


def lambda_handler(event, context):

    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        }
    )

    # fetch page contents
    # page = requests.get(url)

    # parse page and isolate price block
    # tree = html.fromstring(page.content)
    # pricePath = tree.xpath()

    # extract price as float

    # insert/update dynamodb
    session = boto3.Session(profile_name='default')
    dynamodb = session.client('dynamodb')

    response = dynamodb.scan(
        TableName='bpc-check'
    )

    for i in response['Items']:
        print(json.dumps(i))

    while 'LastEvaluatedKey' in response:
        response = dynamodb.scan(
            TableName='bpc-check',
            ExclusiveStartKey=response['LastEvaluatedKey']
        )

        for i in response['Items']:
            print(json.dumps(i))


def extract_price_as_float(text):
    #price = text.encode('utf8')
    return float(re.sub(r"[^0-9\.]+", "", text))
