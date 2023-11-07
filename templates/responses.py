from rest_framework.response import Response


def OK(data):
    return Response({"status": "OK", "code": 200, "data": data})

def BadRequest(errors):
    return Response({"status": "Bad request", "code": 400, "error": errors}, status=400)

def NotFound(errors):
    return Response({"status": "Bad request", "code": 404, "error": errors}, status=404)

def InternalServerError(errors):
    return Response({"status": "Internal server error", "code": 500, "error": errors}, status=500)


class BadRequestExcep(Exception):
    pass

class NotFoundExcep(Exception):
    pass


def endpoint(func):
    def view(*args, **kwargs):
         
        try:
            returned_value = func(*args, **kwargs)
            return returned_value
        except BadRequestExcep as err:
            return BadRequest(str(err))
        except NotFoundExcep as err:
            return NotFound(str(err))
        except Exception as err:
            return InternalServerError(str(err))
         
         
    return view 