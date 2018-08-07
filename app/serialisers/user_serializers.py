from marshmallow import Schema, fields, post_load
import datetime as dt


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)


if __name__ == "__main__":

    user = User(name="Monty", email="monty@python.org")
    user1 = User(name='hhh', email='133@qq.com')
    schema = UserSchema()
    users = [user, user1]
    result = schema.dump(users, many=True)
    print(result.data)

    json_result = schema.dumps(user)
    print(json_result.data)
