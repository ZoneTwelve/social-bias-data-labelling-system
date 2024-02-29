from extensions import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    sentence_id = db.Column(db.Integer, unique=True)
    biased_sentence = db.Column(db.Text, nullable=False)
    tac = db.Column(db.Text)
    source = db.Column(db.String(120))
    identity = db.Column(db.String(120))

class QuestionGroup(db.Model):
    question_group_id = db.Column(db.Integer, primary_key=True)
    identity = db.Column(db.Text)
    bias_comment = db.Column(db.Text)
    non_bias_comment = db.Column(db.Text)
    malice_comment = db.Column(db.Text)
    non_malice_comment = db.Column(db.Text)


class LabeledData(db.Model):
    label_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    sentence_id = db.Column(db.Integer, db.ForeignKey('question.sentence_id'), nullable=False)
    isBias = db.Column(db.Boolean)
    isMalice = db.Column(db.Boolean)
    updateAt = db.Column(db.DateTime)
    visitAt = db.Column(db.DateTime)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
