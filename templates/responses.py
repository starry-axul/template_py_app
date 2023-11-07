from rest_framework.response import Response

def OK(data):
    return Response({"status": "OK", "code": 200, "data": data})

def BadRequest(errors):
    return Response({"status": "Bad request", "code": 400, "error": errors}, status=400)

def InternalServerError(errors):
    return Response({"status": "Internal server error", "code": 500, "error": errors}, status=500)