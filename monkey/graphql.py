import logging
from flask import Blueprint, request, jsonify
from .schema import schema

gql_bp = Blueprint('app', __name__)


@gql_bp.route('/graphql', methods=['POST'])
def graphql():
    result = schema.execute(request.get_data(as_text=True))

    if result.errors:
        return str(result.errors), 400

    return jsonify(result.to_dict())
