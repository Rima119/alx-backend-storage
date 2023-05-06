#!/usr/bin/env python3
"""Task 15's module"""
from pymongo import MongoClient


def log_stats(nginx_collection):
    """Provides some stats about Nginx logs stored in MongoDB"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def print_top_ips(server_collection):
    """Prints statistics of the top 10 of the most
     present IPs in the collection nginx
     of the database logs"""
    print('IPs:')
    request_logs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))


if __name__ == '__main__':
    '''Main function.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)
    print_top_ips(client.logs.nginx)
