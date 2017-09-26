#!/usr/bin/python

from flask import Flask, g, jsonify, redirect, request
app = Flask(__name__)

@app.route('/ambassador/auth', methods=['POST'])
def root():
    return ('', 200)

@app.route('/health')
def health():
    return ("OK", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
