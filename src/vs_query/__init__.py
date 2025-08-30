from flask import Flask
from vs_query.server import app
import os



os.getenv("COMMIT_SHA")
os.getenv("COMMIT_BRANCH")

VERSION = "{}-{}".format(os.getenv("COMMIT_BRANCH"),os.getenv("COMMIT_SHA"))

VS_URL = os.getenv("VS_URL")


from vs_query import routes
