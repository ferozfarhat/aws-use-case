from flask import flask

app = flask(_name_)

@app.route('/')
def hello_devops():
    return 'hello, devops!'

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.o', port=8000)
