"""
View Classes for the API. We recommend to use MethodView inherited classes
"""

# Import flask utilities
from flask.views import MethodView
from flask.globals import request
from flask.json import jsonify

# Import extensions
from myapp.extensions import db

# Import models
from .models import User

"""
MethodView Class
"""


class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            list_users = User.query.all()
            if list_users:
                return jsonify(list_users), 200
        else:
            user = User.query.filter_by(id=user_id).first()
            if user:
                return jsonify(user), 200
        return '', 204

    def post(self):
        data = request.get_json()

        username = data['username']
        email = data['email']

        user = User.query.filter_by(username=username).first(
        ) or User.query.filter_by(email=email).first()

        if user:
            return 'Exists', 502

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return '', 201

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass
