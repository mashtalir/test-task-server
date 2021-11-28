user_schema = {
        'type':'object',
        'properties':{
            'username':{
                'type':'string',
                'maxLength':32,
                'minLength':8,
                },
            "email": {
                "title": "Email address",
                "type": "string",
                "pattern": "^\\S+@\\S+\\.\\S+$",
                "format": "email",
                "minLength": 6,
                "maxLength": 127
            },
            'is_admin':{
                'type':'boolean', 
            }
        }
    }
