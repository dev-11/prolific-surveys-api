from uuid import UUID


def is_uuid_valid(uuid):
    try:
        version = UUID(uuid).version
        # nil UUID has version None
        return False if version is None else True
    except (AttributeError, ValueError, TypeError):
        return False
