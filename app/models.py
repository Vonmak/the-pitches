from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
# from datetime import datetime 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    # comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    # upvotes = db.relationship('upVote', backref = 'user', lazy = 'dynamic')
    # downvotes = db.relationship('downvote', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
     
    
    
class Pitch(db.Model):
    '''
    '''
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    # description = db.Column(db.String(), index = True)
    # title = db.Column(db.String())
    category_id = db.Column(db.String(255), nullable=False)
    # comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    # upvotes = db.relationship('upVote', backref = 'pitch', lazy = 'dynamic')
    # downvotes = db.relationship('downvote', backref = 'pitch', lazy = 'dynamic')

    
    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(pitch_id=id).all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}' 


# class Comment(db.Model):
    
#     __tablename__ = 'comments'

#     id = db.Column(db.Integer,primary_key = True)
#     comment= db.Column(db.String)
#     pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
#     username =  db.Column(db.String)
#     votes= db.Column(db.Integer)
    

#     def save_comment(self):
#         '''
#         Function that saves comments
#         '''
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def clear_comments(cls):
#         Comment.all_comments.clear()

#     @classmethod
#     def get_comments(cls,id):
#         comments = Comment.query.filter_by(pitch_id=id).all()

#         return comments
    
# class PitchCategory(db.Model):
#     '''
#     Function that defines different categories of pitches
#     '''
#     __tablename__ ='pitch_categories'


#     id = db.Column(db.Integer, primary_key=True)
#     name_of_category = db.Column(db.String(255))
#     category_description = db.Column(db.String(255))

#     @classmethod
#     def get_categories(cls):
#         '''
#         This function fetches all the categories from the database
#         '''
#         categories = PitchCategory.query.all()
#         return categories
    
    
# class upVote(db.Model):
#     __tablename__ = 'upvotes'

#     id = db.Column(db.Integer,primary_key=True)
#     upvote = db.Column(db.Integer,default=1)
#     pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

#     def save_upvotes(self):
#         db.session.add(self)
#         db.session.commit()


#     def add_upvotes(cls,id):
#         upvote_pitch = upVote(user = current_user, pitch_id=id)
#         upvote_pitch.save_upvotes()

    
#     @classmethod
#     def get_upvotes(cls,id):
#         upvote = upVote.query.filter_by(pitch_id=id).all()
#         return upvote

#     @classmethod
#     def get_all_upvotes(cls,pitch_id):
#         upvotes = upVote.query.order_by('id').all()
#         return upvotes

#     def __repr__(self):
#         return f'{self.user_id}:{self.pitch_id}'



# class downvote(db.Model):
#     __tablename__ = 'downvotes'

#     id = db.Column(db.Integer,primary_key=True)
#     downVote = db.Column(db.Integer,default=1)
#     pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

#     def save_downvotes(self):
#         db.session.add(self)
#         db.session.commit()


#     def add_downvotes(cls,id):
#         downvote_pitch = downvote(user = current_user, pitch_id=id)
#         downvote_pitch.save_downvotes()

    
#     @classmethod
#     def get_downvotes(cls,id):
#         downVote = downvote.query.filter_by(pitch_id=id).all()
#         return downVote

#     @classmethod
#     def get_all_downvotes(cls,pitch_id):
#         downVote = downvote.query.order_by('id').all()
#         return downVote

#     def __repr__(self):
#         return f'{self.user_id}:{self.pitch_id}'