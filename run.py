import pymongo
from sanic import Sanic
from app import bp
from app.config_file import SERVER_SETTINGS
# import asyncio

app = Sanic(__name__)
app.blueprint(bp)

client = pymongo.MongoClient(host='localhost', port=27017)
test = client.test


# request middleware
@app.middleware('request')
async def print_on_request(request):
    print("I print when a request is received by the server")


# response middleware
@app.middleware('response')
async def print_on_response(request, response):
    response.headers["Server"] = "Fake-Server"
    response.headers["content-type"] = "application/json"
    print("I print when a response is returned by the server")


# async def notify_server_started_after_five_seconds():
#     await asyncio.sleep(5)
#     print('Server successfully started!')

# app.add_task(notify_server_started_after_five_seconds())

if __name__ == "__main__":
    print("app-config:", app.config.keys())
    print(client.test.runoob)
    app.run(**SERVER_SETTINGS)
