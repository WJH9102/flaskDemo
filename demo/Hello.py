import random
from flask import Flask, request, render_template, redirect
import qrcode
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/qr')
def qrcode1():
    return render_template("qrcode.html")


@app.route('/qrtool', methods=['GET', 'POST'])
def qrcode_tool():
    file_list = os.listdir("./static")
    if len(file_list) > 50:
        for file in file_list:
            path_file = os.path.join("./static", file)
            if os.path.isfile(path_file):
                os.remove(path_file)
    path = random.randint(0, 10000)
    content = request.args['content']
    img = qrcode.make(content)
    img.save("static/{}.jpg".format(path))
    return redirect("/static/{}.jpg".format(path))


if __name__ == '__main__':
    app.run(port=8880, debug=True)
