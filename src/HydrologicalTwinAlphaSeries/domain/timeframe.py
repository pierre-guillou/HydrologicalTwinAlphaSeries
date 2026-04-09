"""Temporal support for the domain model.

``TimeFrame`` describes a simulation or analysis period attached to a
:class:`~HydrologicalTwinAlphaSeries.domain.Compartment.Compartment`.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import numpy as np


@dataclass
class TimeFrame:
    """Temporal context for a compartment or analysis.

    Parameters
    ----------
    date_ini : datetime
        Start of the period (inclusive).
    date_end : datetime
        End of the period (exclusive for daily generation).
    timestep : str
        Temporal resolution: ``"daily"`` (default) or ``"monthly"``.
    """

    date_ini: datetime
    date_end: datetime
    timestep: str = "daily"

    # ------------------------------------------------------------------
    # Derived helpers
    # ------------------------------------------------------------------

    @property
    def n_days(self) -> int:
        """Number of calendar days in the period."""
        return (self.date_end - self.date_ini).days

    def date_range(self) -> np.ndarray:
        """Generate a datetime64 array spanning the period.

        Returns
        -------
        np.ndarray
            Array of ``datetime64[D]`` values from *date_ini* (inclusive) to
            *date_end* (exclusive).
        """
        return np.arange(
            np.datetime64(self.date_ini),
            np.datetime64(self.date_end),
            dtype="datetime64[D]",
        )

    # ------------------------------------------------------------------
    # Alternate constructors
    # ------------------------------------------------------------------

    @classmethod
    def from_years(
        cls,
        syear: int,
        eyear: int,
        month: int = 8,
        day: int = 1,
        timestep: str = "daily",
    ) -> "TimeFrame":
        """Create a TimeFrame from hydrological-year boundaries.

        Parameters
        ----------
        syear, eyear : int
            Start and end *hydrological* years.
        month : int
            Month marking the start of the hydrological year (default 8 = August).
        day : int
            Day of month (default 1).
        timestep : str
            Temporal resolution (default ``"daily"``).
        """
        return cls(
            date_ini=datetime(syear, month, day),
            date_end=datetime(eyear, month, day),
            timestep=timestep,
        )

    # ------------------------------------------------------------------
    # Representation
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"TimeFrame({self.date_ini:%Y-%m-%d} → {self.date_end:%Y-%m-%d}, "
            f"timestep={self.timestep!r})"
        )
