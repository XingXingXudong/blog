# coding: utf-8

from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Xudong'}
    posts = [
            {
                'author': {'nickname': 'Xudong'},
                'body': 'Beautiful dat in Portland!'
                },
            {
                'author': {'nickname': 'xudong'},
                'body': 'Halo Flask'
                }
            ]
    
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)
