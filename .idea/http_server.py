from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def hello():
    return "Hello World!"

def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # handle the request here
    return Response(status=200)

context = ('server.crt', 'server.key')

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
    app.run(host='x91765wu.beget.tech', port=443, debug=True)