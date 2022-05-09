from flask import Flask, request, render_template, jsonify
import base64
import json
# import os

from model_run import mirnet_run

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


app = Flask(__name__)

@app.route('/')
def index():
        return ("This is MIRNet-API")

@app.route('/mirnet-api', methods=['GET', 'POST'])
@cross_origin()
def test():
    if request.method == 'POST':
        img_base64 = request.get_json()
        
        decode = open('IMAGE.png', 'wb')
        decode.write(base64.b64decode(img_base64['png']))
        
        img_path = 'IMAGE.png'
        
        mirnet_run(img_path)
        
        with open("output_image.png", "rb") as image2string:
          converted_bytes = base64.b64encode(image2string.read())
        
        converted_string = 'data:image/png;base64,' + converted_bytes.decode('utf-8')
        
        response = {"refined_image": converted_string}
        
        
        return jsonify(response)
    return render_template('index.html')



if __name__ == '__main__':
    # port = os.environ.get('PORT', '5000')
    # app.run(debug=False, host='0.0.0.0', port=port)
    app.run()