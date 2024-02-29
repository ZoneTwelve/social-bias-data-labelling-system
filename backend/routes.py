from flask import Blueprint, request, jsonify
from extensions import db  # Adjust this import according to your project structure
from models import User, Question, LabeledData  # Adjust this import according to your project structure

# Define the blueprint
api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()  # More robust way to handle JSON data
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully', 'user': {'user_id': new_user.user_id, 'username': new_user.username}}), 201

@api_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_data = [{'user_id': user.user_id, 'username': user.username} for user in users]
    return jsonify(users_data), 200

@api_blueprint.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    user.username = username
    db.session.commit()
    return jsonify({'message': 'User updated successfully', 'user': {'user_id': user.user_id, 'username': user.username}}), 200

@api_blueprint.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

@api_blueprint.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    biased_sentence = data.get('biased_sentence')
    if not biased_sentence:
        return jsonify({'error': 'Biased sentence is required'}), 400

    question = Question(
        sentence_id=data.get('sentence_id'),
        biased_sentence=biased_sentence,
        tac=data.get('tac'),
        source=data.get('source'),
        identity=data.get('identity')
    )
    db.session.add(question)
    db.session.commit()
    return jsonify({'message': 'Question added successfully', 'question': {'sentence_id': question.sentence_id}}), 201

@api_blueprint.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    questions_data = [{'sentence_id': q.sentence_id, 'biased_sentence': q.biased_sentence, 'tac': q.tac, 'source': q.source, 'identity': q.identity} for q in questions]
    return jsonify(questions_data), 200

@api_blueprint.route('/labeled_data', methods=['POST'])
def add_labeled_data():
    data = request.get_json()
    sentence_id = data.get('sentence_id')
    isBias = data.get('isBias')
    isMalice = data.get('isMalice')

    # Basic validation
    if sentence_id is None:
        return jsonify({'error': 'Sentence ID is required'}), 400
    if isBias is None or isMalice is None:
        return jsonify({'error': 'isBias and isMalice fields are required'}), 400

    labeled_data = LabeledData(
        sentence_id=sentence_id,
        isBias=isBias,
        isMalice=isMalice,
        updateAt=data.get('updateAt'),  # Optional
        visitAt=data.get('visitAt')  # Optional
    )
    db.session.add(labeled_data)
    db.session.commit()
    return jsonify({'message': 'Labeled data added successfully', 'labeled_data': {'label_id': labeled_data.label_id}}), 201

@api_blueprint.route('/labeled_data', methods=['GET'])
def get_labeled_data():
    labeled_data_entries = LabeledData.query.all()
    data = [{
        'label_id': ld.label_id,
        'sentence_id': ld.sentence_id,
        'isBias': ld.isBias,
        'isMalice': ld.isMalice,
        'updateAt': ld.updateAt,
        'visitAt': ld.visitAt,
        'createAt': ld.createAt
    } for ld in labeled_data_entries]
    return jsonify(data), 200

@api_blueprint.route('/labeled_data/<int:label_id>', methods=['PUT'])
def update_labeled_data(label_id):
    labeled_data = LabeledData.query.get_or_404(label_id)
    data = request.get_json()

    labeled_data.isBias = data.get('isBias', labeled_data.isBias)
    labeled_data.isMalice = data.get('isMalice', labeled_data.isMalice)
    labeled_data.updateAt = data.get('updateAt', labeled_data.updateAt)
    labeled_data.visitAt = data.get('visitAt', labeled_data.visitAt)

    db.session.commit()
    return jsonify({'message': 'Labeled data updated successfully', 'labeled_data': {'label_id': labeled_data.label_id}}), 200

@api_blueprint.route('/labeled_data/<int:label_id>', methods=['DELETE'])
def delete_labeled_data(label_id):
    labeled_data = LabeledData.query.get_or_404(label_id)
    db.session.delete(labeled_data)
    db.session.commit()
    return jsonify({'message': 'Labeled data deleted successfully'}), 200


