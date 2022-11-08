from flask import Flask, request, jsonify, abort
import traceback
import statistics as s
import sys

def abort_msg(e):
    error_class = e.__class__.__name__ # error class
    detail = e.args[0]

    # generate the error message
    errMsg = "[{}] {}.".format(error_class, detail)
    # return 500 code
    abort(500, errMsg)

app = Flask(__name__)
# api = Api(app)
@app.route('/')
def hello():
    return 'Hello TeaHouse'

@app.route('/sampling', methods=['GET', 'POST'])
def sampling():
    if request.method == 'GET':
        mean = request.args.get('mean', 0)
        std_dev = request.args.get('std_dev', 0)
        arr_len = request.args.get('arr_len', 0)

    elif request.method == 'POST':
        mean = request.form['mean']
        std_dev = request.form['std_dev']
        arr_len = request.form['arr_len']

    try:
        samples = s.NormalDist(mu=float(mean), sigma=float(std_dev)).samples(int(arr_len))
        return jsonify(samples)

    except Exception as e:
        abort_msg(e)


if __name__ == '__main__':
    init_host = '127.0.0.1'
    app.run(host=init_host, port=12345)