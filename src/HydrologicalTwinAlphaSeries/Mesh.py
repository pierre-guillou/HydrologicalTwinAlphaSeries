import warnings

warnings.warn(
    "Importing Mesh from the package root is deprecated. "
    "Use HydrologicalTwin facade instead.",
    DeprecationWarning,
    stacklevel=2,
)

from HydrologicalTwinAlphaSeries.domain.Mesh import Mesh

__all__ = ["Mesh"]