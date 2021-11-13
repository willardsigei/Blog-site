from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User,Blog,Comment
from .forms import BlogForm,UpdateProfile,CommentForm
from ..requests import getQuotes

@main.route('/',methods=['GET'])
def index():
    getquotes=getQuotes()
    return render_template('index.html',getquotes=getquotes)



@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def newComment(id):
    blog = Blog.query.filter_by(id = id).all()
    blogComments = Comment.query.filter_by(blog_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(blog_id=id, comment=comment, user=current_user)
        new_comment.saveComment()
    return render_template('newComment.html', blog=blog, blog_comments=blogComments, comment_form=comment_form)



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


@main.route('/user/<uname>')
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



@main.route('/blog/newBlog',methods = ['GET','POST'])
@login_required
def newBlog():
    blogForm = BlogForm()
    if blogForm.validate_on_submit():
        titleBlog=blogForm.blogTitle.data
        description = blogForm.blogDescription.data
        newBlog = Blog(title_blog=titleBlog, description=description, user= current_user)
        newBlog.save_blog()
        return redirect(url_for('main.allBlogs'))
    title = 'New Blog'
    return render_template('new_blogs.html', title=title, blog_form=blogForm)
@main.route('/blog/allblogs', methods=['GET', 'POST'])
@login_required
def allBlogs():
    blogs = Blog.get_all_blogs()
    return render_template('blogs.html', blogs=blogs)


@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteComment(id):
    comment =Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    flash('comment succesfully deleted')
    return redirect (url_for('main.allBlogs'))


@main.route('/deleteblog/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteBlog(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.allBlogs'))   
