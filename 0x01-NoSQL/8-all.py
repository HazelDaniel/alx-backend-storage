#!/usr/bin/env python3
""" this module Performs MongoDB operations with python using pymongo """


def list_all(mongo_collection):
    """ Lists all documents in a collection using python """
    documents = mongo_collection.find()

    if not documents.count():
        return []
    return documents
