from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Selamat datang"

@app.route("/generate_triangle", methods=['POST'])
def generate_triangle():
    data = request.get_json()
    num = data.get("number") 
    result = [];
    lenStr = str(num);
    for i in range(1, len(str(num))+1):
        result.append(lenStr[:i].ljust(len(lenStr),0))

    return str(result)

@app.route("/generate_odds", methods=['POST'])
def generate_odds():
    data = request.get_json()
    num = data.get("number")
    odds = [ x for x in range(1, num+1) if x %2 !=0] 
    return str(odds)

@app.route("/generate_primes", methods=['POST'])
def generate_primes():
    data = request.get_json()
    num = data.get("number")
    primes =[]
    for n in range(2, num+1):
        for i in range(2, n+1):
            if n % 2 ==0:
                break
            else:
                primes.append(n)
        
    print(data.get("number"))
    return str(primes)



if __name__ == '__main__':
    app.run(debug=True)