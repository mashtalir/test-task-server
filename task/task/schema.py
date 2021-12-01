user_schema = {
    'type': 'object',
    'properties': {
        'username': {
            'type': 'string',
            'maxLength': 32,
            'minLength': 8,
            'pattern': '^[A-Za-z][A-Za-z0-9_]{7,29}$'
        },
        "email": {
            "title": "Email address",
            "type": "string",
            "pattern": "^\\S+@\\S+\\.\\S+$",
            "format": "email",
            "minLength": 11,
            "maxLength": 127
        },
        'is_admin': {
            'type': 'boolean',
        }
    }
}
group_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'maxLength': 32,
            'minLength': 1,
            'pattern': '^(.|\s)*[a-zA-Z]+(.|\s)*$'
        },
        'description': {
            'type': 'string',
            'maxLength': 200,
            'minLength': 1,
            'pattern': '^(.|\s)*[a-zA-Z]+(.|\s)*$'
        },
        'users_to_add': {
            'type': 'array'
        }
    }
}
