#!/usr/bin/env python3
""" This module peforms MongoDB operations with python using pymongo """


def update_topics(mongo_collection, name, topics):
    """ this changes all topics of a school document based on the name """
    operation = {"$set": {"topics": topics}}

    mongo_collection.update_many({"name": name}, operation)
