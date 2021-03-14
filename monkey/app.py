import logging
from flask import Flask, jsonify, request

from .schema import schema
from . import db


logging.basicConfig(level=logging.DEBUG)

db.connect_monkey()
db.insert_data_for_query()

app = Flask(__name__)
app.secret_key = b'secret monkey'


@app.route('/graphql', methods=['POST'])
def graphql():
    result = schema.execute(request.get_data(as_text=True))
    app.logger.info(result)
    if result.errors:
        return str(result.errors), 400
    return jsonify(result.to_dict())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
