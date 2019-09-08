def validate_request(request):
    """
    Function to validate simple client request
    :param request: raw client request
    :return: bool value - validation solution

    - Example::
        {'action': 'echo', 'time': ''}
    """
    if 'action' in request and 'time' in request:
        return True
    else:
        return False
