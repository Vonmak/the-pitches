from flask import render_template, request, abort, url_for, redirect
from . import main
from ..models import Pitch, User
from .forms import UpdateProfile, PitchForm
from .. import db, photos
from flask_login import login_required, current_user



@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - The Best Pitching Website'
    
    return render_template('index.html',title = title)


#this section consist of the category_id root functions

@main.route('/interview/pitches/')
def interview():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.filter_by().first()
    interviewpitch = Pitch.query.filter_by(category_id = "interviewpitch")
    title = 'Interview Pitches'  
    return render_template('interview.html', title = title,interviewpitch= interviewpitch, pitches = pitches )

@main.route('/lines/pitches/')
def lines():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pick Up Lines'

    pitches = Pitch.query.filter_by().first()
    pickuplines = Pitch.query.filter_by(category_id= "pickuplines")

    return render_template('lines.html', title = title,pickuplines= pickuplines, pitches =pitches)

@main.route('/promotion/pitches/')
def promotion(): 
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Promotion Pitches'

    pitches = Pitch.query.filter_by().first()
    promotionpitch = Pitch.query.filter_by(category_id = "promotionpitch")

    return render_template('promotion.html', title = title,promotionpitch= promotionpitch ,pitches = pitches)


@main.route('/product/pitches/')
def product():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    pitches = Pitch.query.filter_by().first()
    productpitch = Pitch.query.filter_by(category_id = "productpitch")
    return render_template('product.html', title = title,productpitch= productpitch,pitches = pitches )
 
#  end of category_id root functions


@main.route('/pitches/new/', methods = ['GET','POST'])
# @login_required
def new_pitch():
    form = PitchForm()
    # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        category_id = form.category_id.data
        new_pitch = Pitch(user_id=current_user.id, title = title,description=description,category_id=category_id)
        new_pitch.save_pitch()
        
        
        return redirect(url_for('main.index'))
    return render_template('pitch.html',form=form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
# @login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


