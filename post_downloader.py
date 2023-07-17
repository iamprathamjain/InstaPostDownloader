from flask import Flask, render_template, request, json, jsonify

from insta import download_instagram_reel
import os
from random import randint as ri


app = Flask(__name__)

@app.route("/", methods=['POST', 'PUT', 'GET'])
def home():
    if request.method == 'POST':
        id=ri(1,30000)
        
        # url = json.loads(request.data.decode('utf-8'))
        url=request.form.get('insta_url')
        # print(url['url'])
        print(url,"________",id)
        details=download_instagram_reel(url)
        print(details.get('id'))
        files = os.listdir(f'just'+str(details.get('id')))
        print(files)

        

        
        








        #return jsonify({'a': 'static/2023-07-06_18-57-45_UTC.jpg'})
        return render_template('landing_page2.html')
    else:
        return render_template('landing_page2.html')

if __name__ == '__main__':
    app.run(debug=1,host='0.0.0.0')
