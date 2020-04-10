def get_key(content, key, logger=None):
    """Check is a key value is present or not in a dictionary.
       if logger is set the value will be logged in info is present
       and warning if not present."""
    if not content:
        if logger:
            logger.warning("Empty dictionary detected")
        return None
    if not isinstance(content, dict):
        if logger:
            logger.warning("Invalid dictionary detected")
        return None

    if not key in content:
        if logger:
            logger.warning("key {} was not found in the dictionary".format(key))
        return None
    else:
        value = content[key]
        if logger:
            logger.info('key "{}" = "{}"'.format(key, value))
        return value
