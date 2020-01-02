from flask import Flask,jsonify 
from primeHelper import rightTruPrime,leftTruPrime
app = Flask(__name__) 
  
@app.route('/hello/<name>') 
def hello_name(name): 
   return 'Hello %s!' % name 

@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 
    if(rightTruPrime(num) & leftTruPrime(num)):
        result='true'
    else:
        result='false'

    return jsonify({'Is two sided prime ': result}) 
  
if __name__ == '__main__': 
   app.run()   

