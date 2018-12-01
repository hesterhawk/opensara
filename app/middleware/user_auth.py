from flask import redirect, url_for, request
from flask_login import current_user

from functools import wraps

"""
    TODO: permissions for every module used in this project
"""

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("=========ARGS")
        print(kwargs)
        print("=========/ARGS")
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login', next=request.url))            
        return f(*args, **kwargs)

    return decorated_function