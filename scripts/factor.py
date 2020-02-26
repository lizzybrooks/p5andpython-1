#!/usr/bin/env python3
# File: factor.py
# ---------------
# http://localhost:8000/scripts/factor.py?number=96294
#
# {
#    success: true,
#    number: 96294000,
#    factors: [2, 2, 2, 2, 3, 5, 5, 5, 11, 1459]
# }
#
# If the number param is missing, malformed, or out of range,
# then the respond will just be this:
#
# {
#    success: false
# }


import cgi, os, sys
import json

def computeFactorization(n):
    """
    Computes the prime factorization of what's assumed to
    be a reasonably small positive number.  We require
    it be reasonably small so the algorithm returns fairly
    quickly.
    """
    factors = []
    factor = 2
    while n > 1:
        while n % factor == 0:
            factors.append(factor)
            n /= factor
        factor += 1
    return factors

def extractRequestParameter(param):
    """
    Returns the value attached to the key within the query string
    of the request URL.  If, for instance, the query string is
    a=123&b=hello, then extractRequestParam("a") would return "123",
    extractRequestParam("b") would return "hello", and extractRequestParam("c")
    would return None
    """
    params = cgi.FieldStorage()
    if param not in params: return None
    return params[param].value


def handleRequest():
    """
    Invoked to factor a reasonably small positive number
    and returns with a payload that includes its factorization.
    """
    number = extractRequestParameter("number")
    response = {}
    response["success"] = number.isdigit() and int(number) > 0 and int(number) <= 100000
    if response["success"]:
        response["number"] = int(number)
        response["factors"] = computeFactorization(int(number))

    answer = json.dumps(response)
    print("Content-Length: " + str(len(answer)))
    print("Content-Type: application/json")
    print()
    print(answer)
#
#
handleRequest()