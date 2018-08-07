from sanic import Blueprint
from app.views.test import SimpleView

bp = Blueprint('my_blueprint', url_prefix="/v1/my_blueprint")


bp.add_route(SimpleView.as_view(), '/')
