from datetime import datetime


def make_request(action, data, token):
    return {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data,
        'token': token
    }


def make_response(request, code, data=None):
    """
    Function for preparing a request
    :param request: client request
    :param code: server-answer code
    :param data: server-answer data
    :return: dictionary request
    """
    return {
        'data': data,
        'time': request.get('time'),
        'action': request.get('action'),
        'code': code,
    }
