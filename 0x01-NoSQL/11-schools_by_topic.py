#!/usr/bin/env python3
""" This module performs MongoDB operations with python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of documents having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
