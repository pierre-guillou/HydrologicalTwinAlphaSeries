import warnings

warnings.warn(
    "Importing Compartment from the package root is deprecated. "
    "Use HydrologicalTwin facade instead.",
    DeprecationWarning,
    stacklevel=2,
)

from HydrologicalTwinAlphaSeries.domain.Compartment import Compartment

__all__ = ["Compartment"]