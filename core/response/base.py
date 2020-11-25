import jsonpickle
from flask import Response
from core.utils import utils


def full_custom_response(code: int,
                         method: str,
                         message: str,
                         data: object,
                         datas: []):
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
    response = {
        "meta": {
            "code": 500,
            "api_version": utils.api_version(),
            "method": http_method,
            "message": internal_server_
        },
        "page_info": {
            "page_from": 0,
            "page_to": 0
        },
        "data": {
            "message": internal_server_,
            "item": None,
            "items": []
        }
    }
    data = jsonpickle.encode(response, unpicklable=False)
    return Response(data, status=500, mimetype='application/json')


def success(http_method: str):
    success_processing = "Success Processing Request"
    response = {
        "meta": {
            "code": 200,
            "api_version": utils.api_version(),
            "method": http_method,
            "message": success_processing
        },
        "page_info": {
            "page_from": 0,
            "page_to": 0
        },
        "data": {
            "message": success_processing,
            "item": None,
            "items": []
        }
    }
    data = jsonpickle.encode(response, unpicklable=False)
    return Response(data, status=200, mimetype='application/json')


def success_with_data_single(data: object, http_method: str):
    success_processing = "Success Processing Request"
    response = {
        "meta": {
            "code": 200,
            "api_version": utils.api_version(),
            "method": http_method,
            "message": success_processing
        },
        "page_info": {
            "page_from": 0,
            "page_to": 0
        },
        "data": {
            "message": success_processing,
            "item": data,
            "items": []
        }
    }
    data = jsonpickle.encode(response, unpicklable=False)
    return Response(data, status=200, mimetype='application/json')


def success_with_data_list(data: any, http_method: str):
    success_processing = "Success Processing Request"
    response = {
        "meta": {
            "code": 200,
            "api_version": utils.api_version(),
            "method": http_method,
            "message": success_processing
        },
        "page_info": {
            "page_from": 0,
            "page_to": 0
        },
        "data": {
            "message": success_processing,
            "item": None,
            "items": data
        }
    }
    data = jsonpickle.encode(response, unpicklable=False)
    return Response(data, status=200, mimetype='application/json')


def success_with_data_list_and_single(data: object, datas: any, http_method: str):
    success_processing = "Success Processing Request"
    response = {
        "meta": {
            "code": 200,
            "api_version": utils.api_version(),
            "method": http_method,
            "message": success_processing
        },
        "page_info": {
            "page_from": 0,
            "page_to": 0
        },
        "data": {
            "message": success_processing,
            "item": data,
            "items": datas
        }
    }
    data = jsonpickle.encode(response, unpicklable=False)
    return Response(data, status=200, mimetype='application/json')
