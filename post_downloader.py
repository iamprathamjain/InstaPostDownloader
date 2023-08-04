from flask import Flask, render_template, request, json, jsonify

from insta import download_instagram_reel
import os,shutil
from random import randint as ri


app = Flask(__name__)

@app.route("/", methods=['POST', 'PUT', 'GET'])
def home():
    if request.method == 'POST':
        
        url=request.form.get('insta_url')
        
        details=download_instagram_reel(url)
        print(details.get('id'))
        downloadedPath=f'just'+str(details.get('id'))
        files = os.listdir(downloadedPath)
        # print(files)
        sources=[]

        for file in files:
            # if file.endswith('jpg') or file.endswith('mp4'):
            # print(file)
            old_file_path = os.path.join(downloadedPath,file) 
            new_file_path = os.path.join('static','insta',str(details.get('id'))+'-ID-'+file)
            os.rename(old_file_path, new_file_path)

        staticPath=os.listdir('static/insta')
        for i in staticPath:
            if(int(i[:4])==(details.get('id'))) and ( i.endswith('jpg') or i.endswith('mp4')):
                sources.append(os.path.join('static','insta',i).replace('\\','/'))       
                
        print(sources)
        #return jsonify({'a': 'static/2023-07-06_18-57-45_UTC.jpg'})
        return render_template('landing_page2.html',sources=sources,post_caption=details.get('caption'),post_owner=details.get('owner'),post_likes=details.get('likes'),post_comments=details.get('comments'),post_url=details.get('url'))
    else:
        return render_template('landing_page2.html')

if __name__ == '__main__':
    app.run(debug=1,host='0.0.0.0',port=1212)
