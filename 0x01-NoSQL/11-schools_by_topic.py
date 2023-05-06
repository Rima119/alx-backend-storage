#!/usr/bin/env python3
"""Task 11's module"""


def schools_by_topic(mongo_collection, topic: str) -> list:
    """Returns the list of school having a specific topic"""
    topic_manager = {
        'topics':{
            '$elemMatch':{
                '$eq': topic
            },
        },
    }
    return [doc for doc in mongo_collection.find({"topics": topic})]
