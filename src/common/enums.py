"""
Common Enum subclasses that can be use to hold model choices
(including `ugettext_lazy` values)

# Examples:


"""

from __future__ import unicode_literals

import decimal
import enum

import six


class ChoiceEnumMeta(enum.EnumMeta):
    """Metaclass for ChoiceEnum classes."""

    def __new__(mcs, cls, bases, attrs):
        """Create new ChoiceEnum class. Add default string conversion method
        and custom __new__ method for member instances.
        """
        already_applied = any(isinstance(base, mcs) for base in bases)

        base_type = attrs.pop("base_type", object)

        if not already_applied:

            if "__str__" not in attrs:

                def __str__(self):
                    return six.text_type(self.value)

                attrs["__str__"] = __str__

            if "__new__" not in attrs:

                def __new__(cls, value, label=None):
                    if base_type is object:
                        obj = base_type.__new__(cls)
                    else:
                        obj = base_type.__new__(cls, value)
                    obj._value_ = value
                    obj.label = label if label is not None else six.text_type(value)
                    return obj

                attrs["__new__"] = __new__

        # Python 3: "base_type" class attribute cannot be considered a member:
        if "base_type" in getattr(attrs, "_member_names", []):
            attrs._member_names.remove("base_type")

        return enum.EnumMeta.__new__(mcs, cls, bases, attrs)

    def __dir__(cls):
        return enum.EnumMeta.__dir__(cls) + [
            "choices",
            "values",
            "labels",
            "label_to_value",
        ]

    @property
    def choices(cls):
        """Retrieve a tuple of all choices - (value, label) pairs."""
        # pylint: disable=not-an-iterable
        return tuple((obj.value, obj.label) for obj in cls)

    @property
    def label_to_value(cls):
        """Retrieve a dict of all choices - (label, value) pairs.
        We lowercase the keys to make the search easier and
        keep the case in enum definition intact.
        """
        # pylint: disable=not-an-iterable
        return {obj.label.lower(): obj.value for obj in cls}

    @property
    def values(cls):
        """Retrieve a tuple of all values."""
        # pylint: disable=not-an-iterable
        return tuple(obj.value for obj in cls)

    @property
    def labels(cls):
        """Retrieve a tuple of all labels."""
        # pylint: disable=not-an-iterable
        return tuple(obj.label for obj in cls)


class StringEnum(six.text_type, enum.Enum):
    """Enum where members are strings."""


class DecimalEnum(decimal.Decimal, enum.Enum):
    """Enum where members are Decimal objects."""


@six.python_2_unicode_compatible
class GenericChoiceEnum(six.with_metaclass(ChoiceEnumMeta, enum.Enum)):
    """ChoiceEnum with type restriction on values / instances."""


@six.python_2_unicode_compatible
class IntChoiceEnum(six.with_metaclass(ChoiceEnumMeta, enum.IntEnum)):
    """ChoiceEnum with values / instances restricted to be integers."""

    base_type = int


@six.python_2_unicode_compatible
class StringChoiceEnum(six.with_metaclass(ChoiceEnumMeta, StringEnum)):
    """ChoiceEnum with values / instances restricted to be strings."""

    base_type = six.text_type


@six.python_2_unicode_compatible
class DecimalChoiceEnum(six.with_metaclass(ChoiceEnumMeta, DecimalEnum)):
    """ChoiceEnum with values / instances restricted to be Decimal objects."""

    base_type = decimal.Decimal
