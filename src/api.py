from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import PutError

from os import getenv

from dotenv import load_dotenv
load_dotenv()


class Banana(Model):
    class Meta:
        access_key = getenv("AWS_ACCESS_KEY_ID")
        secret_key = getenv("AWS_SECRET_ACCESS_KEY")
        aws_region = getenv("AWS_REGION")
        
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