from flask import request
from core.response import base


def home():
    ini_data_object = None
    return base.full_custom_response(404, request.method, "Not Found", ini_data_object, [])


def internal_server_error():
    return base.internal_server_response(request.method)
