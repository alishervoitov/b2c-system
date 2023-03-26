from rest_framework import renderers
import json
from email import charset
class UserRenderer(renderers.JSONRenderer):

    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None, set_default=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'Error': data})
        else:
            response = json.dumps(data, default=set_default)
        return response