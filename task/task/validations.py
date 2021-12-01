from .schema import user_schema, group_schema
from jsonschema import validate


def user_schema_validation(data):
    try:
        validate(data, user_schema)
    except Exception as exp:
        print(exp)
        return 'not valid'


def group_schema_validation(data):
    try:
        validate(data, group_schema)
    except Exception as exp:
        print(exp)
        return 'not valid'
