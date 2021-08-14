
from app.requests import get_category, get_news_objects, get_articles, get_headlines
from flask import render_template, request, redirect, url_for
from . import main



@main.route('/')
def base():
    source_data = get_news_objects()
    headlines = get_headlines()

    return render_template('index.html', sources = source_data, headlines = headlines)


@main.route('/source/<id>')
def index(id):

    ident= id.replace(" ", "-")

    articles = get_articles(ident)

    return render_template('articles.html', articles = articles)

@main.route('/categories/<name>')
def category(name):

    category = get_category(name)
    
    return render_template('category.html', category = category)