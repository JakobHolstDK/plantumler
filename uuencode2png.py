# read the jsoon file and convert it to a png file

import json
import base64
import os
import sys

def uuencode2png(json_file, output_file='output.png'):
    """
    Convert a uuencoded image from a JSON file to a PNG file.

    Args:
      json_file: A JSON file containing a uuencoded image.

    Returns:
      A PNG file containing the decoded image.

    Raises:
      Exception: If any error occurs during the process.
    """
    try:
        # Read the JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)
        # Decode the image
        decoded_image = base64.b64decode(data['image'])
        # Write the image to a PNG file
        with open(outout_file, 'wb') as f:
            f.write(decoded_image)
    except Exception as e:
        raise e
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python uuencode2png.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    outout_file = sys.argv[2]
    uuencode2png(json_file, output_file)

# Usage: python uuencode2png.py <json_file> output.png
# Example: python uuencode2png.py image.json

# 2024-07-05 13:34:00 - Last updated by: Jakob Holst


