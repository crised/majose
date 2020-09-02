from flask import Flask
from flask import render_template, request

import data_parser

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    """
    Unique HTTP Endpoint of the application
    If the request is POST and it receives a valid form
    input, it will filter the countries.

    If the request is GET it will show a filtered list
    by a default threshold value.
    :return: the template with arguments
    """
    if request.method == 'POST':
        try:
            thres = float(request.form['value'])
        except ValueError:
            return render_template('hello.html', items=None)
        return render_template('hello.html', items=data_parser.get_filtered_countries(thres), thres=thres)

    return render_template('hello.html', items=data_parser.get_filtered_countries(), thres=7)


if __name__ == "__main__":
    app.run()
