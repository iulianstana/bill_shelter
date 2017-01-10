from app import app


@app.route('/', methods=['GET'])
def __index__():
    return "Hello World"

