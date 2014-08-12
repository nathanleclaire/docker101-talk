from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(
    host=os.environ.get('REDIS_1_PORT_6379_TCP_ADDR'),
    port=int(os.environ.get('REDIS_1_PORT_6379_TCP_PORT'))
)

@app.route('/')
def hello():
    redis.incr('hits')
    return '<pre>hey everyone!  i have been seen %s times.</pre>' % redis.get('hits')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
