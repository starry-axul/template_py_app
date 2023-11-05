from rest_framework.response import Response

def ResOK(data):
    return Response({"status": "OK", "code": 200, "data": data})

def ResBadRequest(errors):
    return Response({"status": "Bad request", "code": 400, "error": errors}, status=400)