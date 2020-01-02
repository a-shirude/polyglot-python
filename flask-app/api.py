from flask import Flask,jsonify 
from primeHelper import rightTruPrime,leftTruPrime
app = Flask(__name__) 
  
@app.route('/api', methods = ['GET']) 
def apiWelcome(): 
   return 'Welcome to Flask API demo : Two sided prime number.'

@app.route('/api/<int:num>', methods = ['GET']) 
def isTwoSidedPrime(num): 
    if(rightTruPrime(num) & leftTruPrime(num)):
        result='true'
    else:
        result='false'

    return jsonify({str(num) + ' is two sided prime? ': result}) 
  
if __name__ == '__main__': 
   app.run()   

