def zipmap(keys, values):
    if not keys or not values:
        return {}

    result = zipmap(keys[1:], values[1:])

    result[keys[0]] = values[0]
    return result