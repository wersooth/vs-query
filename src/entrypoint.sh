#!/bin/sh
uwsgi -w vs_query:app --http-socket :5000 --py-autoreload 1
