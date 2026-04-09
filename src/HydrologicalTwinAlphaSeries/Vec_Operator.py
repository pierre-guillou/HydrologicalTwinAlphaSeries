import warnings

warnings.warn(
    "Importing Comparator/Extractor/Operator from the package root is deprecated. "
    "Use HydrologicalTwin facade instead.",
    DeprecationWarning,
    stacklevel=2,
)

from HydrologicalTwinAlphaSeries.services.Vec_Operator import Comparator, Extractor, Operator

__all__ = ["Comparator", "Extractor", "Operator"]