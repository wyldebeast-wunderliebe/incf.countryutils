"""incf.countryutils: A convenience API for country code transformations."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("incf.countryutils")
except PackageNotFoundError:
    __version__ = "unknown"

