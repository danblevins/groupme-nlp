
def groupby_transform(data, groupby_column: str, transform_column: str):
    return data.groupby([groupby_column]).transform(transform_column)