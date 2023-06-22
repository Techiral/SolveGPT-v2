# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os

from flask_minify  import Minify

from apps import create_app

app = create_app()

DEBUG = app.config['DEBUG'] 


if __name__ == "__main__":
    app.run(debug=True)
