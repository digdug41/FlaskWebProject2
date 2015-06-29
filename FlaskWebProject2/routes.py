from flask import Flask, url_for;
from app import app;

#Server
@app.route('/')

def hello():
    createLink = "<a href='"+ url_for("create") + "'>Create a question</a>";
    diggyhtml1="""<!DOCTYPE html>

    <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <link href="/diggy.css" rel="stylesheet" />
    <head>
        <meta charset="utf-8" />
        <title></title>
    </head>
    <body>
        """+ createLink +"""<p>test</p>
    </body>
    </html>""";


    """Renders a sample page."""
    return diggyhtml1

#Server/create
@app.route('/wibble')
def create():
    return"<h2>This is the create page!</h2>";

@app.route('/goodbye')

def goodbye():
    return "<h2>GOODBYE</h2>"

#Server/question/<title>
@app.route('/question/<title>')
def question(title):
    return "<h2>" + title + "</h2>";

@app.route('/diggy.css')
def diggycss():
    return "body{}p{color:hotpink;"