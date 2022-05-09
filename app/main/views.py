from flask import render_template, request
from . import main
from ..models import Pitch, User



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
    # pitch = Pitch.query.filter_by().first()
    interviewpitch = Pitch.query.filter_by(category_id = "interviewpitch")
    title = 'Interview Pitches'  
    return render_template('interview.html', title = title,pitches= interviewpitch )

@main.route('/lines/pitches/')
def lines():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pick Up Lines'

    # pitch = Pitch.query.filter_by().first()
    lines = Pitch.query.filter_by(category_id="lines")

    return render_template('lines.html', title = title,pitches= lines )

@main.route('/promotion/pitches/')
def promotion():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Promotion Pitches'

    # pitch = Pitch.query.filter_by().first()
    promotionpitch = Pitch.query.filter_by(category_id = "promotionpitch")

    return render_template('promotion.html', title = title,pitches= promotionpitch )


@main.route('/product/pitches/')
def product():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    # pitch = Pitch.query.filter_by().first()
    productpitch = Pitch.query.filter_by(category_id = "productpitch")
    return render_template('product.html', title = title,pitches= productpitch )
 
#  end of category_id root functions