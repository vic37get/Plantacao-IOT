def changeLabel(data, metric, labelPositive, labelNegative):
    if data == metric:
        data = labelPositive
    else:
        data = labelNegative
    return data
