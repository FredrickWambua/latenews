from flask import render_template
from . import main

# Application-wide error handler
@main.app_errorhandler(404)
def we_not_here(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('weNotHere.html'),404