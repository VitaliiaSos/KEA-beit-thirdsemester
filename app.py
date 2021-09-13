from re import template
from flask import Flask
from flask.templating import render_template_string
import connector as cn

app = Flask(__name__)

template = """
<!doctype html>
<title>Hello from Flask</title>
<h1>temperature is: {{ temperature }}, humidity is: {{humidity}}, pressure is: {{pressure}}!</h1>
"""


@app.route('/')
def index():
    return render_template_string(template, temperature=getdata()[0], humidity=getdata()[1], pressure=getdata()[2])


def getdata():

    thisConn = cn.dbconnect()
    myCursor = thisConn.cursor()
    data=""" SELECT Temperature, Humidity, BarometricPressure FROM hatdata
    ORDER BY DateandTime DESC
    LIMIT 1;
    """
    myCursor.execute(data)
    test = myCursor.fetchone()
    return test


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')