from flask import render_template, request, redirect, url_for
from . import main

@main.route('/')
def base():
    return render_template('base.html')
