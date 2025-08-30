from vs_query import app
from flask import render_template
from vs_query import VERSION, VS_URL
import  requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@app.route('/')
def index():
    rsp = query_vs()
    return render_template('index.html',ver=VERSION, url=VS_URL, RESP=rsp)


def query_vs() -> list:
    _url = VS_URL
    try:
        response = requests.get(VS_URL)
    except Exception as ex:
        logger.error(ex)

    print(response.json())
    logging.info(f"Query VS instance: {0}".format(VS_URL))

    return response.json()
