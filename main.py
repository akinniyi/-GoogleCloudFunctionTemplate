from utils import GCP_PROJECT_ID

def main(request):
    """Explain function here.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_data = request.get_json() or request.args
    print(request_data)
    return f'Hello World!'