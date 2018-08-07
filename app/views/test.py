from sanic.views import HTTPMethodView
from sanic.response import json
from app.services.test_service import SimpleViewService
import pymongo
import json as my_json
from app import json_util


def json_load(data):
    return my_json.loads(data, object_hook=json_util.object_hook)


def json_dump(data):
    return my_json.dumps(data, default=json_util.default)


class SimpleView(HTTPMethodView):

    def get(self, request):
        SimpleViewService.do_something()

        # student1 = {
        #     'id': '20170101',
        #     'name': 'Jordan',
        #     'age': 20,
        #     'gender': 'male'
        # }

        # student2 = {
        #     'id': '20170202',
        #     'name': 'Mike',
        #     'age': 21,
        #     'gender': 'male'
        # }

        client = pymongo.MongoClient(host='localhost', port=27017)
        test = client.test

        runoob = test.runoob
        result = runoob.find()
        
        return json(json_dump(list(result)))

    def post(self, request):
        return json('I am post method')

    def put(self, request):
        return json('I am put method')

    def patch(self, request):
        return json('I am patch method')

    def delete(self, request):
        return json('I am delete method')
     