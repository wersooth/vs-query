from vs_query import app
from flask import render_template
from vs_query import VERSION, VS_URL
import  requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@app.route('/')
def index():
    return render_template('index.html',ver=VERSION, url=VS_URL)


def query_vs(url: str) -> list:
    _url = VS_URL
    response = requests.get(VS_URL)

    print(response.json())
    logging.info(f"Query VS instance: {0}".format(VS_URL))
    logging.info(response.json())

    return [item['data'] for item in response.json()]
