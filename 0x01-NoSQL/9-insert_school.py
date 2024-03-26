#!/usr/bin/env python3
""" This module performs MongoDB operations with python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based
       on fields provided in the kwargs parameter"""
    return mongo_collection.insert(kwargs)
