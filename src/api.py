from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import PutError

import boto3
from botocore.exceptions import ClientError

from os import getenv
from dotenv import load_dotenv

load_dotenv()


def get_secrets():
    secrets_name = "ddb-things"
    region_name = "ap-southeast-1"

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)
    if session.region_name == "ap-southeast-1":
        try:
            get_secret_value_response = client.get_secret_value(SecretId=secrets_name)
            secrets = get_secret_value_response["SecretString"].split("\n")
            print("aws")
            #for i in range(3)
            secrets = {secrets[i]: secrets[i + 1] for i in (range(0, len(secrets), 2))}
        except ClientError as e:
            raise e
    else:
        print("local")
        secrets = {
            "AWS_ACCESS_KEY_ID": getenv("AWS_ACCESS_KEY_ID"),
            "AWS_SECRET_ACCESS_KEY": getenv("AWS_SECRET_ACCESS_KEY"),
            "AWS_REGION": getenv("AWS_REGION"),
        }
    return secrets


class Banana(Model):
    class Meta:
        secrets = get_secrets()
        access_key = secrets["AWS_ACCESS_KEY_ID"]
        secret_key = secrets["AWS_SECRET_ACCESS_KEY"]
        aws_region = secrets["AWS_REGION"]

        table_name = "accad6"
        region = aws_region
        write_capacity_units = 10
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
