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
