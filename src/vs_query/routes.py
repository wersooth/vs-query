from vs_query import app
from flask import render_template
from vs_query import VERSION, VS_URL
import  requests
import logging
from dateutil.parser import parse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MONTH = ["Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "July",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dec"
]


@app.route('/')
def index():
    rsp = query_vs()
    vs_time = parse("{}:{}".format(rsp['date']['hour'],rsp['date']['minute'])).strftime("%H:%M")
    return render_template('index.html',ver=VERSION, url=VS_URL, RESP=rsp, MONTH=MONTH,TIME=vs_time)


def query_vs() -> list:
    import time
    _url = VS_URL
    try:
        response = requests.get(VS_URL)
        resp = response.json()
    except Exception as ex:
        logger.error(ex)
    logging.info(f"Query VS instance: "+ VS_URL)

    return response.json()
