from flask import jsonify, request
from model import *
from config import app


@app.route('/')
def index():
    people = People.getAll()
    serialize = PeopleSchema(many=True)
    data = serialize.dump(people)
    return jsonify(data)


@app.route('/', methods=['POST'])
def create():
    data = request.get_json()

    if People.exist(data.get('pname')):
        return jsonify({"message": "User {pname} already exist".format(pname=data.get('pname'))}), 409

    new_people = People(
        pname=data.get('pname'),
        color=data.get('color')
    )
    new_people.save()
    serializer = PeopleSchema()
    data = serializer.dump(new_people)
    return jsonify(data), 201


@app.route('/<int:id>', methods=['GET'])
def getById(id):
    people = People.getById(id)
    serializer = PeopleSchema()
    data = serializer.dump(people)
    return jsonify(data), 200


@app.route('/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    people = People.getById(id)
    people.delete()
    return jsonify({"message": "Deleted"}), 204


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server(error):
    return jsonify({"message": "There is a problem"}), 500


if __name__ == '__main__':
    app.run(port=80)