def get_status(is_busy):
    return "busy" if (is_busy == False) else "available"


print(get_status(False))