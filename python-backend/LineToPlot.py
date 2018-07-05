from apistar import types, validators


class LineToPlot(types.Type):
    name = validators.String()
    series = validators.Array()
