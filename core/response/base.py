import jsonpickle
from flask import Response
from core.utils import utils


def full_custom_response(code: int, method: str, message: str, data: object, datas: any):
    response = {
        "meta": {
            "code": code,
            "api_version": utils.api_version(),
            "method": method,
            "message": message
        },
        "page_info": {
            "page_from": 0,
            "page_to": 0
        },
        "data": {
            "message": message,
            "item": data,
            "items": datas
        }
    }
    data = jsonpickle.encode(response, unpicklable=False)
    return Response(data, status=code, mimetype='application/json')


def internal_server_response(http_method: str):
    internal_server_ = "Oops, Internal Server Error"
    response = full_custom_response(500, http_method, internal_server_, None, [])
    return response


def unprocessable_entity_response(http_method: str):
    bad_request = "Oops, Unprocessable Entity"
    response = full_custom_response(422, http_method, bad_request, None, [])
    return response


def success(http_method: str):
    success_processing = "Success Processing Request"
    response = full_custom_response(200, http_method, success_processing, None, [])
    return response


def success_with_data_single(data: object, http_method: str):
    success_processing = "Success Processing Request"
    response = full_custom_response(200, http_method, success_processing, data, [])
    return response


def success_with_data_list(data: any, http_method: str):
    success_processing = "Success Processing Request"
    response = full_custom_response(200, http_method, success_processing, None, data)
    return response


def success_with_data_list_and_single(data: object, datas: any, http_method: str):
    success_processing = "Success Processing Request"
    response = full_custom_response(200, http_method, success_processing, data, datas)
    return response
