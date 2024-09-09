from flask import Flask, request
from calc.operations import add, sub, mult, div  # Import the helper functions

app = Flask(__name__)

@app.route('/add')
def do_add():
    """Add a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    """Subtract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def do_div():
    """Divide a by b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
