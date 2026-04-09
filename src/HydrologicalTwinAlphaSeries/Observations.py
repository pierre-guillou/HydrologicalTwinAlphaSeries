import warnings

warnings.warn(
    "Importing Observation/ObsPoint from the package root is deprecated. "
    "Use HydrologicalTwin facade instead.",
    DeprecationWarning,
    stacklevel=2,
)

from HydrologicalTwinAlphaSeries.domain.Observations import Observation, ObsPoint

__all__ = ["Observation", "ObsPoint"]