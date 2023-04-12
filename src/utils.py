from .types import Item

# fmt: off
__all__ = [
    'Formatter',
]
# fmt: on


class Formatter:
    TYPE_CONVERSIONS = {"_S": str, "_I": int, "_R": float, "_B": bool}

    @staticmethod
    def format(data: Item | str | int | bool | float) -> dict:
        """Similarly to aws dynamodb, in order to retain
        types when storing all data as text, we can use keys
        denoting the data type.

        For example,
        {
            "foo": "bar"
        }
        goes to
        {
            "foo": {
                "S": "bar"
            }
        }

        In order to format the types of our data, we will need to
        recursively add keys denoting each data type.
        """
        response = {}
        if isinstance(data, dict):
            for key, value in data.items():
                response[key] = Formatter.format(value)
        else:
            for key, value in Formatter.TYPE_CONVERSIONS.items():
                if isinstance(data, value):
                    return {key: data}
        return response

    @staticmethod
    def unformat(data: dict) -> Item:
        """Oppositely to the format method, this method removes
        type formatting

        Similiar recursion approach, but deleting the type
        keys instead of adding them.

        Also casts values to their correct type.
        """
        response = {}
        for key, value in data.items():
            if key in Formatter.TYPE_CONVERSIONS:
                caster = Formatter.TYPE_CONVERSIONS[key]
                return caster(value)
            else:
                response[key] = Formatter.unformat(value)
        return response
