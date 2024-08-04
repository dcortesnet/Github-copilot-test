def division(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        raise ZeroDivisionError("Denominator cannot be zero.")


