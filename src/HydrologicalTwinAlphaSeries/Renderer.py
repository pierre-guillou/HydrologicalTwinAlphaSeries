import warnings

warnings.warn(
    "Importing Renderer from the package root is deprecated. "
    "Use HydrologicalTwin facade instead.",
    DeprecationWarning,
    stacklevel=2,
)

from HydrologicalTwinAlphaSeries.services.Renderer import Renderer

__all__ = ["Renderer"]