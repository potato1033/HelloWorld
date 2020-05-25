import re

class IgnoreCrsMiddleware(object):
    def process_request(self,request,**karg):
        if re.match(r'^/admin/?$',request.path):
            request.csrf_processing_done = True
            return None