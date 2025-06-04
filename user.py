from data import db, User

def create_new_user(username, password):
    new_user = User(username = username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user