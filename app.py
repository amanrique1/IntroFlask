from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello world'

"""
Se puede dejar vacio o poner:
-string
-int
-float
-path (ejem user/uniandes/isis llega uniandes isis)
"""
@app.route('/user/<float:userid>', methods=['GET','POST'])
def getUser(userid):
    if request.method == 'POST':
        pass
    return 'Double %f' % userid

@app.route('/userget/<path:info>')
def getUserInfo(info):
    return info

if __name__ =='__main__':
    app.run(host='localhost',port=5000,debug=True)