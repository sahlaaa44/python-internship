class InvalidMarkError(Exception):
    pass

mark = -35

if mark < 0:
    raise InvalidMarkError("Mark cannot be negative")
