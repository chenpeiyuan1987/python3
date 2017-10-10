from flask import Flask;
from flask import request;

app = Flask(__name__)

@app.route('/hello')
def hello () :
    return 'hello';

@app.route('/book/list')
def bookList () :
    return 'books list';

@app.route('/book/info/<int:id>')
def bookInfo (id) :
    return 'book[%s]\'s info.' % id;

@app.route('/args')
def args () :
    return str(request.args);

if __name__ == '__main__':
    app.run(debug=True);
