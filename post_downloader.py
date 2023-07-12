from flask import Flask,render_template,request,json,send_file,jsonify



app = Flask(__name__)

@app.route("/",methods=['POST','PUT','GET'])
def home():
    if request.method=='POST':
        url=json.loads(request.data.decode('utf-8'))
        print(url['url'])
        return jsonify({'a':'static/reels/2023-06-22_09-57-15_UTC.jpg'})

        
    else:
        return render_template('landing_page2.html')
    

if __name__ == '__main__':
    app.run(debug=True)