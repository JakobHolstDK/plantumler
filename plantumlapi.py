# Python flask api that get a text file in a rest api call and returns a uuencoded file

import flask
from flask import request, jsonify

import os
import base64
import subprocess
import sys

app = flask.Flask(__name__)

@app.route('/api/v1/plantuml', methods=['POST'])
def plantuml():
  """

  Generate a PlantUML diagram from a text file and return it as a uuencoded file.
  An example curl command to test this function is:
  curl -X POST -H "Content-Type: text/plain" --data-binary @<file>.txt http://localhost:5000/api/v1/plantuml

  This function receives a POST request with a text file in the request body.
  It creates a temporary file to store the text, generates a PlantUML diagram
  using the `plantuml` command-line tool, encodes the resulting image as a
  uuencoded file, and returns it as a JSON response.

  Returns:
    A JSON response containing the uuencoded image.

  Raises:
    Exception: If any error occurs during the process.
  """
  try:
    # Get the text file from the request
    text = request.get_data().decode("utf-8")
    # Create a temp file to store the text
    with open('temp.txt', 'w') as f:
      f.write(text)
    # Generate the plantuml diagram
    subprocess.run(["java", "-jar", "plantuml.jar", "temp.txt"])
    # Encode the image
    with open('temp.png', 'rb') as f:
      encoded_string = base64.b64encode(f.read())
    # Remove the temp files
    os.remove('temp.txt')
    os.remove('temp.png')
    return jsonify({'image': encoded_string.decode('utf-8')})
  except Exception as e:
    return jsonify({'error': str(e)})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
