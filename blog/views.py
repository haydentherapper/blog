from flask import render_template, redirect, url_for
from blog import app

import re

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

urlfinder = re.compile(r'(&#39;)(https?://\S+)(&#39;)')
code = open('code_snippets.py').read()

@app.template_filter('add_href')
def add_href_filter(html):
    return urlfinder.sub(r'<a href="\2">\1\2\3</a>', html)

@app.route("/")
def home():
    global code
    highlighted_code = highlight(code, PythonLexer(), HtmlFormatter())
    return render_template('index.html', code=highlighted_code)

@app.route("/blog/")
def blog():
    return redirect(url_for('home'))
