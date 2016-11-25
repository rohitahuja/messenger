import requests

GRAPH_API_URL = 'https://graph.facebook.com/v2.8'

class MessengerException(Exception):
    pass


class MessengerError(object):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)

    def raise_exception(self):
        raise MessengerException(
            getattr(self, 'error_data', self.message)
        )


class MessengerClient(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def send(self, request):
        """
        Sends a message given a MessengerRequest type object.
        """
        params = {
            'access_token': self.access_token
        }
        method = getattr(requests, request.method)
        response = method(
            request.graph_api_endpoint,
            params=params,
            json=request.to_dict()
        )
        if response.status_code != 200:
            MessengerError(
                **response.json()['error']
            ).raise_exception()
        return response.json()


# TODO change the name to this to just messenger object
# TODO add more error checking based on api
class BaseMessengerObject(object):
    def to_dict(self):
        raise NotImplementedError


class BaseMessengerRequest(BaseMessengerObject):
    """
    Base class for request objects in messenger.
    Must have request_type attribute set.
    """

    request_type = None

    REQUEST_METHODS = (
        'get', 'post', 'delete'
    )

    def __init__(self, method):
        if method not in self.REQUEST_METHODS:
            raise ValueError('<BaseMessengerRequest> method attr should be one of %s' % str(self.REQUEST_METHODS))
        self.method = method

    @property
    def graph_api_endpoint(self):
        if not self.request_type:
            raise ValueError('<BaseMessengerRequest> must have request_type constant set')

        return '{}/me/{}'.format(GRAPH_API_URL, self.request_type)

    def serialize(self):
        return json.dumps(self.to_dict())
