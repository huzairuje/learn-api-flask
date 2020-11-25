from flask import request
from core.response import base as base_response


def home():
    ini_data_object = None
    return base_response.full_custom_response(404, request.method, "Not Found", ini_data_object, [])


def internal_server_error():
    return base_response.internal_server_response(request.method)


def succes():
    data = {
        "name": "uje",
        "age": 27,
        "address": "Dago"
    }
    datas = [{
        "id": 1,
        "skill": "golang"
    },
        {
            "id": 2,
            "skill": "php"
        },
        {
            "id": 3,
            "skill": "java"
        },
        {
            "id": 4,
            "skill": "python"
        }
    ]
    return base_response.success_with_data_list_and_single(data, datas, request.method)
