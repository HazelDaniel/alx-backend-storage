#!/usr/bin/env python3
""" This module performs MongoDB operations with python using pymongo """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    top_average = mongo_collection.aggregate([

        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top_average
