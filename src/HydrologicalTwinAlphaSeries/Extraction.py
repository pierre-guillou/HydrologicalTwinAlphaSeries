import warnings

warnings.warn(
    "Importing Extraction/ExtractionPoint from the package root is deprecated. "
    "Use HydrologicalTwin facade instead.",
    DeprecationWarning,
    stacklevel=2,
)

from HydrologicalTwinAlphaSeries.domain.Extraction import Extraction, ExtractionPoint

__all__ = ["Extraction", "ExtractionPoint"]