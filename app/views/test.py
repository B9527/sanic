from sanic.views import HTTPMethodView
from sanic.response import json
from app.services.test_service import SimpleViewService


class SimpleView(HTTPMethodView):

    def get(self, request):
        SimpleViewService.do_something()
        return json('I am get method')

    def post(self, request):
        return json('I am post method')

    def put(self, request):
        return json('I am put method')

    def patch(self, request):
        return json('I am patch method')

    def delete(self, request):
        return json('I am delete method')
     