from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import PutError

from os import getenv

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "ddb-things"
    region_name = "ap-southeast-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    return secret
    # Your code goes here.
value = get_secret()
valueSplit = value.split("\n")

class Banana(Model):
    class Meta:
        access_key = valueSplit[1]
        secret_key = valueSplit[3]
        aws_region = valueSplit[5]
        
        table_name = "accad6"
        # Specifies the region
        region = "ap-southeast-1"
        # Specifies the write capacity
        write_capacity_units = 10
        # Specifies the read capacity
        read_capacity_units = 10

    username = UnicodeAttribute(hash_key=True)
    banana = NumberAttribute()


if not Banana.exists():
    Banana.create_table(wait=True)


def createBanana(user: str, bananaNo: int = 0) -> Banana:
    createItem = Banana(user, banana=bananaNo)
    try:
        createItem.save(condition=Banana.username.does_not_exist())
    except PutError:
        pass
    return createItem


def readBananaFull(user: str) -> Banana:
    userItem = Banana.get(user)
    return userItem


def readBananaNum(user: str) -> int:
    bananaQty = Banana.get(user).banana
    return bananaQty


def addBanana(user: str, bananas: int) -> None:
    userItem = readBananaFull(user)
    userItem.update(actions=[Banana.banana.set(bananas)])
    return userItem


def deleteUser(user: str) -> None:
    deleteTarget = Banana.get(user)
    deleteTarget.delete()
    return None

createBanana("api-test")