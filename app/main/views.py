from app.requests import get_news_objects, get_articles
from flask import render_template, request, redirect, url_for
from . import main



@main.route('/')
def base():
    source_data = get_news_objects()

    return render_template('index.html', sources = source_data)

@main.route('/source/<id>')
def articles(id):

    ident= id.replace(" ", "-")

    articles = get_articles(ident)

    return render_template('articles.html', articles = articles)


