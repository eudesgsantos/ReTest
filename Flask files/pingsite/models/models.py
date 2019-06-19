from pingsite import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lugar = db.Column(db.String(50), nullable=False)
    problema = db.Column(db.String(120), nullable=False)
    extra = db.Column(db.String(120))
    def __repr__(self):
        return f"User('{self.lugar}', '{self.problema}', '{self.extra}' )"
class Login(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), nullable = False)
    user_id = db.Column(db.String(150), unique = True, nullable=False)
    def __repr__(self):
        return f"Login('{self.email}', '{self.nome}')"
