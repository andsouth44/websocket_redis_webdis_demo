
from flask import Flask, render_template, request
import time
import redis

app = Flask(__name__)

@app.route("/test_msg", methods=['GET', 'POST'])
def test_msg():
	#return "hello world"
    if request.method == 'POST':
		    # connect to redis server
        r = redis.client.StrictRedis(host='192.168.199.85', port=6379, db=0, password=None)
        time.sleep(2)

	    # publish message to redis using group name passed in via ident argument
        r.publish(666, 'You have started a server side function')

        time.sleep(2)

	    # publish message to redis using group name passed in via ident argument
        r.publish(666, 'Function running, please wait......')

        time.sleep(2)

         # publish message to redis using group name passed in via ident argument
        r.publish(666, 'Function still running, almost done.......')

        time.sleep(2)
        return render_template("func_finish.html")

    elif request.method == 'GET':
    	return render_template("layout.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
