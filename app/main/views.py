from flask import render_template, request, redirect, url_for
from . import main
from app import app

@main.route('/')
def base():
    return render_template('base.html')
