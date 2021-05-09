# -*- coding: utf-8 -*-

from json import dumps

import flask
from flask import request, jsonify

from minio import Minio
from minio.error import S3Error

import models.minio as models

app = flask.Flask(__name__)
app.config["DEBUG"] = True

client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)


@app.route('/buckets', methods=['GET'])
def home():
    buckets = client.list_buckets()
    return jsonify(list(map(lambda bucket:models.Bucket(bucket.name).serialize(), buckets)))

@app.route('/buckets/<name>', methods=['GET'])
def process(name):
    return '{"result":"OK", "filename":"'+name+'"}'

app.run()