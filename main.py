from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.data.decode('utf-8')
    with open('Shaxzod.txt', 'a') as f:
        f.write(data + '\n')
    return 'Success', 200

if __name__ == '__main__':
    app.run(host='http://185.100.54.38:5000/upload', port=5000, debug=False)


