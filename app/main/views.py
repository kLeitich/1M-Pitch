from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Role,Pitch,Comment
from flask_login import current_user, login_required
from .forms import  NewComment, UpdateProfile,NewPitch
from .. import db,photos


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitchs = Pitch.query.all()
    return render_template('index.html',pitchs=pitchs)




@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
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


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitch/<uname>/update',methods = ['GET','POST'])
@login_required
def new_pitch(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = NewPitch()

    if form.validate_on_submit():
        category = form.category.data
        pitchContent = form.pitchContent.data
        pitchAuthor = form.pitchAuthor.data
        new_pitch = Pitch(category=category,pitchContent=pitchContent,pitchAuthor=pitchAuthor)
        
        new_pitch.save_pitch()
        return redirect(url_for('main.index',uname=user.username))
    

   
    return render_template('pitch.html',form =form)


@main.route('/comment/<uname>/update',methods = ['GET','POST'])
@login_required
def new_comment(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = NewComment()

    if form.validate_on_submit():
        comment= form.commentNew.data
        comment_author=form.comment_author.data
        new_comment = Comment(comment=comment,comment_author=comment_author)

        new_comment.save_comment()
        return redirect(url_for('main.new_comment',uname=user.username))

    comments = Comment.query.all()
    

    return render_template('comment.html',form =form,comments=comments)


@main.route('/category/interview')
def interview():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('category/interview.html')


@main.route('/category/product')
def product():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('category/product.html')

@main.route('/category/promotion')
def promotion():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('category/promotion.html')

@main.route('/category/sales')
def sales():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('category/sales.html')


# @main.route('/thumbup/<int:id>', methods=['GET', 'POST'])
# @login_required
# def thumbup(id):
#     pitch = Pitch.query.get(id)
#     if pitch is None:
#         abort(404)
#     thumbup = Voteup.query.filter_by(user_id=current_user.id, pitch_id=id).first()
#     if thumbup is not None:
#         db.session.delete(thumbup)
#         db.session.commit()
#         return redirect(url_for('main.index'))
#     new_thumbup = Voteup(user_id=current_user.id,pitch_id=id)
#     db.session.add(new_thumbup)
#     db.session.commit()
#     return redirect(url_for('main.index'))
