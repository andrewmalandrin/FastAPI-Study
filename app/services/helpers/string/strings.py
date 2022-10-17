def convert_snake_to_camel(snake_string: str) -> str:
    components = snake_string.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])
