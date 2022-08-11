class QueryParameters:
    query_params = {
        'num': 4,
        'min': 0,
        'max': 7,
        'col': 1,
        'base': 10,
        'format': 'plain',
        'rnd': 'new'
    }


parameters = QueryParameters()


def get_query_params():
    return parameters.__class__.query_params

