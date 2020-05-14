from flask import Flask, jsonify, request, make_response,send_from_directory
app = Flask('test')
@app.route('/api/v1/test/',methods=['GET'])
def test():
    return "Flask OK",200
if __name__ == '__main__':
    app.run()