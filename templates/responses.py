from rest_framework.response import Response
from rest_framework import status


def OK(data):
    return Response({"status": "OK", "code": status.HTTP_200_OK, "data": data})


def Created(data):
    return Response({"status": "OK",
                     "code": status.HTTP_201_CREATED,
                     "data": data},
                    status=status.HTTP_201_CREATED)


def BadRequest(errors):
    return Response({"status": "Bad request",
                     "code": status.HTTP_400_BAD_REQUEST,
                     "error": errors},
                    status=status.HTTP_400_BAD_REQUEST)


def NotFound(errors):
    return Response({"status": "Bad request",
                     "code": status.HTTP_404_NOT_FOUND,
                     "error": errors},
                    status=status.HTTP_404_NOT_FOUND)


def InternalServerError(errors):
    return Response({"status": "Internal server error",
                     "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                     "error": errors},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
