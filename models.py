from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer, db.ForeignKey('round.id', ondelete='CASCADE'),primary_key=True)
    content = db.Column(db.Text(), nullable=False)

class Answer(db.Model):
    question_id = db.Column(db.Integer,db.ForeignKey('question.id',ondelete='CASCADE'),primary_key=True)
    question_round = db.Column(db.Integer,db.ForeignKey('question.round',ondelete='CASCADE'),primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    score = db.Column(db.Float, nullable=False)
    essay = db.Column(db.Boolean, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    sum = db.Column(db.Integer, nullable=False)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), nullable=False)
    pass_rate = db.Column(db.Float)