from rest_framework.views import exception_handler


def error_handler(exception, context):
    """Handle bad requests"""
    
    response = exception_handler(exception, context)

    if response is not None:
        response.data['status_code'] = response.status_code
    
    return response
