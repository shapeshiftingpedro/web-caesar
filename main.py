from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form =""" <!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/encryptor" method="post">
      
      Rotate by:<input type="text" name="rot" value="0" />
      <textarea name="text"></textarea>
      <br/>
      <input type="submit" value="Encrypt It!" />
      
      </form>
    </body>
</html>
"""

@app.route("/encryptor" , methods=['POST'])
def encrypt():
    rot = int(request.form["rot"])
    text = str(request.form["text"])
    content = rotate_string(text, rot)
    return "<h1>" + content + "</h1>"
@app.route("/")
def index():
    return form

app.run()