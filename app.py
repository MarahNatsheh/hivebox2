from flask import Flask, jsonify

app = Flask(__name__)

VERSION = 'v0.0.1'

@app.route('/version')
def version():
    """
    Returns the version of the application.
    
    Returns:
        dict: A dictionary containing the version of the application.
    """
    return jsonify({"version": VERSION})

if __name__ == '__main__':
    print(f"App version: {VERSION}")
    app.run(host='0.0.0.0', port=5000)
